import re


def regex_word(length, text):
    word = re.sub(r'\b\w{0,'+str(length)+r'}\b', '', text)
    return " ".join(word.split())
