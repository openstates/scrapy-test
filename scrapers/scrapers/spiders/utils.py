import re
import requests
from scrapy import Selector

custom_headers = {
    "user-agent": "openstates.org"
}


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
