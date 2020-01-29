def odd_even_list(ls):
    for i in range(len(ls)):
        if isinstance(ls[i], int) is False:
            return []
        elif ls[i] % 2 == 0:
            ls[i] = "EVEN"
        else:
            ls[i] = "ODD"
    return ls
