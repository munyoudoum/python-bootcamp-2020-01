r=[]
a=input("Enter a sentence: ")
while a != "GENERATE":
    r.append(a)
    a=input("Enter a sentence: ")
else:
    for i in r:
        print("<p>{}</p>".format(i))
    if not r:
        print("Nothing to display.")