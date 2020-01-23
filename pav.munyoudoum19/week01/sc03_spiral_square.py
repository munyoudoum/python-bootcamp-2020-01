def spiral_square(map):
    r = 0
    c = 0
    n = len(map)
    while r < n:
        for i in range(c, n):
            print(map[r][i], end=" ")
        r += 1
        for i in range(r, n):
            print(map[i][n-1], end=" ")
        for i in range(n-2, c - 1, -1):
            print(map[n-1][i], end=" ")
        n -= 1
        for i in range(n-1, r-1, -1):
            print(map[i][c], end=" ")
        c += 1
