import requests


def get_html(link):
    return requests.get(link).text
