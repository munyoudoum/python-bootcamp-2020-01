import re


def regex_alpha_k(text):
    search = re.compile(r'[^a-kA-K0-5]').search
    return not bool(search(text))
