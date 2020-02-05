import re


def regex_urls(text):
    return re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
