class MatrixModule():
    @staticmethod
    def gen_empty_matrix(height, width):
        if height <= 0 or width <= 0:
            return None
        w = [''] * width
        res = []
        for _ in range(height):
            res.append(w)
        return res

    @staticmethod
    def gen_value_matrix(value, height, width):
        if height <= 0 or width <= 0:
            return None
        w = [value] * width
        res = []
        for _ in range(height):
            res.append(w)
        return res
