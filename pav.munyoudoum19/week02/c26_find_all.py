def find_all(ls, value):
    res = []
    for i in range(len(ls)):
        if value == ls[i]:
            res.append(i)
    if not res:
        return None
    else:
        return res


def find_first(ls, value):
    if value in ls:
        return ls.index(value)
    else:
        return None
