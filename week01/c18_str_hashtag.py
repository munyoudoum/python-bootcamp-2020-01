text=input("Enter something: ")
if "#" not in text:
    print(text)
else:
    for i in range(len(text)):
        if text[i]=="#":
            print(text[:i])
            break