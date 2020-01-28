def list_number(start, end, reversed=False):
    res = []
    if reversed is False:
        for i in range(start, end+1):
            res.append(i)
    else:
        for i in range(end, start-1, -1):
            res.append(i)
    return res
