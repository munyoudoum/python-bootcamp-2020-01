title = input("Enter a title: ")
if title.strip() != "":
    print("<h1>{}</h1>".format(title))
else:
    print("Nothing to display.")
