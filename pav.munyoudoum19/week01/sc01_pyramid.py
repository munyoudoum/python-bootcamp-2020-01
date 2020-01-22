def pyramid(level, symbol, is_reverse=False):
    if level <= 1:
        print("Invalid parameters")
    else:
        if is_reverse == False:
            space = level-1
            num=1
            while space >= 0:
                print(" "*space+symbol*num)
                num+=2
                space-=1
        else:
            space=0
            num = (2 * level-1)
            while space < level:
                print(" "*space+symbol*num)
                num-=2
                space+=1