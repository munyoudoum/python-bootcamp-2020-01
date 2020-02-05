class Reader():
    @staticmethod
    def read(filename):
        f = open(filename, "r")
        return f.read()[:-1]

    @staticmethod
    def readlines(filename):
        f = open(filename, "r")
        return f.read()[:-1].split("\n")
