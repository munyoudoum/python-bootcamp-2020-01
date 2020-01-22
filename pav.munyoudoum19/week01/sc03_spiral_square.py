def spiral_square(map):
    result = []
    n = len(map)
    i = 0
    j = n
    while i < n:
        while j > 1:
            result.append(map[i][-j])
            j -= 1
        while i < (n-1):
            result.append(map[i][-j])
            i += 1
            print(i)
        while j < n:
            result.append(map[i][-j])
            j += 1
    print(result, i, j)


spiral_square([[1,2,3,4],
               [5,6,7,8],
               [9,0,1,2],
               [3,4,5,6]])