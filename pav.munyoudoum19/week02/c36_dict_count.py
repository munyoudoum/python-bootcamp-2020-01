import json


def dict_count(ls):
    d = {}
    for i in ls:
        d[i] = ls.count(i)
    return json.dumps(d)
