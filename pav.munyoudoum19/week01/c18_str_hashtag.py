text = input("Enter something: ")
if "#" not in text:
    print(text)
else:
    for i, item in enumerate(text):
        if text[i] == "#":
            print(text[:i])
            break
