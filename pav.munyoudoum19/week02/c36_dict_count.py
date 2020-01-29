def dict_count(ls):
    d = {}
    for i in ls:
        d[str(i)] = ls.count(i)
    return d
