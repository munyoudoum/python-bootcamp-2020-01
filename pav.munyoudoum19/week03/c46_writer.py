class Writer():
    @staticmethod
    def write(filename, text):
        f = open(filename, "w+")
        f.write(text+"\n")
        f.close()
        return f
    @staticmethod
    def append(filename, text):
        f = open(filename, "a+")
        f.write(text+"\n")
        return f

writer = Writer()

writer.append("abc.txt", "bye!")