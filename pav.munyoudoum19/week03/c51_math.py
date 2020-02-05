class MathsModule():
    @staticmethod
    def get_min(ls):
        return min(ls)

    def get_max(ls):
        return max(ls)

    def get_min_max(ls):
        return (min(ls), max(ls))

    def average(ls):
        return sum(ls) / len(ls)

    def diff(ls):
        return max(ls) - min(ls)
