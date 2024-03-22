import boto3  # noqa
import datetime
import importlib
import json
import jsonschema
import logging
import os
import scrapelib
import uuid
from collections import defaultdict, OrderedDict
from jsonschema import Draft3Validator, FormatChecker

from ..exceptions import ScrapeError, ScrapeValueError, EmptyScrape


@FormatChecker.cls_checks("uri-blank")
def uri_blank(value):
    return value == "" or FormatChecker().conforms(value, "uri")


@FormatChecker.cls_checks("uri")
def check_uri(val):
    return val and val.startswith(("http://", "https://", "ftp://"))


def cleanup_list(obj, default):
    if not obj:
        obj = default
    elif isinstance(obj, str):
        obj = [obj]
    elif not isinstance(obj, list):
        obj = list(obj)
    return sorted(obj)


class BaseModel(object):
    """
    This is the base class for all the Open Civic objects. This contains
    common methods and abstractions for OCD objects.
    """

    # to be overridden by children. Something like "person" or "organization".
    # Used in :func:`validate`.
    _type = None
    _schema = None

    def __init__(self):
        super(BaseModel, self).__init__()
        self._id = str(uuid.uuid1())
        self._related = []
        self.extras = {}

    # validation

    def validate(self, schema=None):
        """
        Validate that we have a valid object.

        On error, this will raise a `ScrapeValueError`

        This also expects that the schemas assume that omitting required
        in the schema asserts the field is optional, not required. This is
        due to upstream schemas being in JSON Schema v3, and not validictory's
        modified syntax.
        ^ TODO: FIXME
        """
        if schema is None:
            schema = self._schema

        # this code copied to openstates/cli/validate - maybe update it if changes here :)
        type_checker = Draft3Validator.TYPE_CHECKER.redefine(
            "datetime", lambda c, d: isinstance(d, (datetime.date, datetime.datetime))
        )
        type_checker = type_checker.redefine(
            "date",
            lambda c, d: (
                isinstance(d, datetime.date) and not isinstance(d, datetime.datetime)
            ),
        )

        ValidatorCls = jsonschema.validators.extend(
            Draft3Validator, type_checker=type_checker
        )
        validator = ValidatorCls(schema, format_checker=FormatChecker())

        errors = [str(error) for error in validator.iter_errors(self.as_dict())]
        if errors:
            raise ScrapeValueError(
                "validation of {} {} failed: {}".format(
                    self.__class__.__name__, self._id, "\n\t" + "\n\t".join(errors)
                )
            )

    def pre_save(self, jurisdiction_id):
        pass

    def as_dict(self):
        d = {}
        for attr in self._schema["properties"].keys():
            if hasattr(self, attr):
                d[attr] = getattr(self, attr)
        d["_id"] = self._id
        return d

    # operators

    def __setattr__(self, key, val):
        if key[0] != "_" and key not in self._schema["properties"].keys():
            raise ScrapeValueError(
                'property "{}" not in {} schema'.format(key, self._type)
            )
        super(BaseModel, self).__setattr__(key, val)


class SourceMixin(object):
    def __init__(self):
        super(SourceMixin, self).__init__()
        self.sources = []

    def add_source(self, url, *, note=""):
        """Add a source URL from which data was collected"""
        new = {"url": url, "note": note}
        self.sources.append(new)


class LinkMixin(object):
    def __init__(self):
        super(LinkMixin, self).__init__()
        self.links = []

    def add_link(self, url, *, note=""):
        self.links.append({"note": note, "url": url})


class AssociatedLinkMixin(object):
    def _add_associated_link(
        self,
        collection,
        note,
        url,
        *,
        media_type,
        on_duplicate="warn",
        date="",
        classification="",
    ):
        if on_duplicate not in ["error", "ignore", "warn"]:
            raise ScrapeValueError("on_duplicate must be 'warn', 'error' or 'ignore'")

        try:
            associated = getattr(self, collection)
        except AttributeError:
            associated = self[collection]

        ver = {
            "note": note,
            "links": [],
            "date": date,
            "classification": classification,
        }

        # keep a list of the links we've seen, we need to iterate over whole list on each add
        # unfortunately this means adds are O(n)
        seen_links = set()

        matches = 0
        for item in associated:
            for link in item["links"]:
                seen_links.add(link["url"])

            if all(
                ver.get(x) == item.get(x) for x in ["note", "date", "classification"]
            ):
                matches = matches + 1
                ver = item

        # it should be impossible to have multiple matches found unless someone is bypassing
        # _add_associated_link
        assert matches <= 1, "multiple matches found in _add_associated_link"

        if url in seen_links:
            if on_duplicate == "error":
                raise ScrapeValueError(
                    "Duplicate entry in '%s' - URL: '%s'" % (collection, url)
                )
            elif on_duplicate == "warn":
                # default behavior: same as ignore but logs an warning so people can fix
                logging.getLogger("openstates").warning(
                    f"Duplicate entry in '{collection}' - URL: {url}"
                )
                return None
            else:
                # This means we're in ignore mode. This situation right here
                # means we should *skip* adding this link silently and continue
                # on with our scrape. This should *ONLY* be used when there's
                # a site issue (Version 1 == Version 2 because of a bug) and
                # *NEVER* because "Current" happens to match "Version 3". Fix
                # that in the scraper, please.
                #  - PRT
                return None

        # OK. This is either new or old. Let's just go for it.
        ret = {"url": url, "media_type": media_type}

        ver["links"].append(ret)

        if matches == 0:
            # in the event we've got a new entry; let's just insert it into
            # the versions on this object. Otherwise it'll get thrown in
            # automagically.
            associated.append(ver)

        return ver
