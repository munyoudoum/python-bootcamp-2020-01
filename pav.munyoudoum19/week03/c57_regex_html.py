import re


def regex_html(text):
    return re.sub('<.*?>', '', text)
