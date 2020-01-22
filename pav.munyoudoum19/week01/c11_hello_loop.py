try:
    num = int(input("Enter a number: "))
    if type(num) == int:
        for i in range(num):
            print("Hello World!")
except ValueError:
    pass
