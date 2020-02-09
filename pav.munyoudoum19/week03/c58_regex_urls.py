import re


def regex_urls(text):
    return re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)

print(regex_urls('<a href="https://w3resource.com">Python</a><a href="http://github.com">'))