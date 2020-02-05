class Writer():
    @staticmethod
    def write(filename, text):
        f = open(filename, "w+")
        f.write(text+"\n")
        f.close()

    @staticmethod
    def append(filename, text):
        f = open(filename, "a+")
        f.write(text+"\n")
