def int_list(ls):
    res = True
    if not ls:
        res = False
    for i in ls:
        if isinstance(i, int) is False:
            res = False
            break
    return res
