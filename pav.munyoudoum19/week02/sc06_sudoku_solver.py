def empty(ls, rowcol):
    for row in range(9):
        for col in range(9):
            if(ls[row][col] == 0):
                rowcol[0] = row
                rowcol[1] = col
                return False
    return True


def checkh(num, r, ls):
    for col in range(9):
        if(ls[r][col] == num):
            return False
    return True


def checkv(num, c, ls):
    for row in range(9):
        if(ls[row][c] == num):
            return False
    return True


def checkx(num, row, col, ls):
    sr = (row // 3) * 3
    sc = (col // 3) * 3
    for row in range(sr, sr+3):
        for col in range(sc, sc+3):
            if ls[row][col] == num:
                return False
    return True


def checkall(num, row, col, ls):
    return checkh(num, row, ls) and checkv(num, col, ls) and \
        checkx(num, row, col, ls)


def sudoku_solver(ls):
    rowcol = [0, 0]
    if empty(ls, rowcol):
        return True
    row = rowcol[0]
    col = rowcol[1]
    for num in range(1, 10):
        if checkall(num, row, col, ls):
            print(ls[row][col], num)
            ls[row][col] = num
            if (sudoku_solver(ls)):
                return ls
            ls[row][col] = 0
    return False
