try:
    num = int(input("Enter a number: "))
    if isinstance(num, int):
        for i in range(num):
            print("Hello World!")
except ValueError:
    pass
