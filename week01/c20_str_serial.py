text=input("Enter something: ")
if text == "":
    print("EMPTY")
else:
    num=0
    result=[]
    for i in text:
        if i != " ":
            result.append(i.upper()+i.lower()*num)
            num+=1
    print("-".join(result))