def gen_chessboard(height=8, width=8):
    if height < 2 or width < 2 or width % 2 != 0 or height % 2 != 0:
        return None
    res = []
    for row in range(height):
        res.append([])
        for col in range(width//2):
            if row % 2 == 0:
                res[row].append(1)
                res[row].append(0)
            else:
                res[row].append(0)
                res[row].append(1)
    return res
