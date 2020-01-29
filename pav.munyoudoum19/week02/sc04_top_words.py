import collections
import re
def top_words(string):
    if not string.strip():
        return []
    ls = string.split(" ")
    indexs = []
    indexe = []
    for word in ls:
        for c in range(0, len(word)):
            if word[c].isalpha():
                indexs.append(c)
                break
    for word in ls:
        for c in range(len(word), 0, -1):
            if word[c-1].isalpha():
                indexe.append(c)
                break
    s = 0
    e = 0
    new = []
    for word in ls:
        if re.search('[a-zA-Z]', word):
            new.append(word[indexs[s]:indexe[e]].lower())
            s += 1
            e += 1
    counts = collections.Counter(new)
    newls = sorted(new, key=counts.get, reverse=True)
    res = list(dict.fromkeys(newls))
    return res[:3]
