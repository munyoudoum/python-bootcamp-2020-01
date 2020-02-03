class Reader():
    @staticmethod
    def read(filename):
        f = open(filename, "r")
        return f.read()[:-2]
    @staticmethod
    def readlines(filename):
        f = open(filename, "r")
        return f.read()[:-2].split("\n")
reader = Reader()
print(reader.read("abc.txt"))
print(reader.readlines("abc.txt"))