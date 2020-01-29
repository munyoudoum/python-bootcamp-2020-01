def sudoku(x):
    for ls in x:
        check = []
        if len(ls) != 9:
            return "Invalid"
        else:
            for num in ls:
                if num < 1 or num > 9:
                    return "Invalid"
                else:
                    check.append(num)
            if sorted(check) != list(range(1, 10)):
                return "Unfinished"

    for col in range(9):
        checkv = []
        for row in range(9):
            checkv.append(x[row][col])
        if sorted(checkv) != list(range(1, 10)):
            return "Unfinished"
    sr = 0
    er = 3
    sc = 0
    ec = 3
    for _ in range(9):
        if sc == 9:
            sr += 3
            er += 3
            sc = 0
            ec = 3
        checkx = []
        for row in range(sr, er):
            for col in range(sc, ec):
                checkx.append(x[row][col])
        sc += 3
        ec += 3
        if sorted(checkx) != list(range(1, 10)):
            return "Unfinished"
    return "Finished"
