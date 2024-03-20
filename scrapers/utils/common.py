import re
import requests
import lxml.html
import logging
from scrapy import Selector


custom_headers = {
    "user-agent": "openstates.org"
}


def url_xpath(url, path, verify=True, user_agent=None):
    headers = {"user-agent": user_agent} if user_agent else None
    res = requests.get(url, verify=verify, headers=headers)
    try:
        doc = lxml.html.fromstring(res.text)
    except Exception as e:
        logging.error(
            f"Failed to retrieve xpath from {url} :: returned:\n"
            f"CONTENT: {res.content} \n"
            f"RETURN CODE: {res.status_code}"
        )
        raise Exception(e)
    return doc.xpath(path)


# get css/xpath wrapper with the response from an url
def lxmlize(url):
    response = requests.get(url, headers=custom_headers)
    return Selector(response)


# remove whitespace, linebreaks, and end parentheses
def clean_text(text):
    newtext = re.sub(r"[\r\n]+", " ", text)
    newtext = re.sub(r"\s{2,}", " ", newtext)
    m = re.match(r"(.*)\(.*?\)", newtext)
    if not m:
        return newtext.strip()
    else:
        return m.group(1).strip()
