class MathsModule():
    @staticmethod
    def get_min(ls):
        return min(ls)

    @staticmethod
    def get_max(ls):
        return max(ls)

    @staticmethod
    def get_min_max(ls):
        return (min(ls), max(ls))

    @staticmethod
    def average(ls):
        return sum(ls) / len(ls)

    @staticmethod
    def diff(ls):
        return max(ls) - min(ls)
