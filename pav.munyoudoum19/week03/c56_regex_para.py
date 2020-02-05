import re


def regex_para(text):
    return re.sub(r" ?\([^)]+\)", "", text)
