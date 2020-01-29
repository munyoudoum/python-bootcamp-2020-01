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
            if sorted(check) == list(range(1, 10)):
                pass
            else:
                return "Unfinished"
    for col in range(9):
        checkv = []
        for row in range(9):
            checkv.append(x[row][col])
        if sorted(checkv) == list(range(1, 10)):
            pass
        else:
            return "Unfinished"
    return "Finished"
