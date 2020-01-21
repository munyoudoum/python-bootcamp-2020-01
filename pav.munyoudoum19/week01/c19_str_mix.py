word=input("Enter a word: ")
if len(word)>2:
    print(word[1::-1]+word[-1:-3:-1])
elif len(word)==2:
    print(word*2)
elif len(word)==1:
    print(word*4)
elif len(word)==0:
    print("0"*4)