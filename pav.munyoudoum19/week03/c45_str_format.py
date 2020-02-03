class StringFormat():
    @staticmethod
    def first(text):
        return text[0]
    @staticmethod
    def last(text):
        return text[-1]
    @staticmethod
    def lower(text):
        return text.lower()
    @staticmethod
    def upper(text):
        return text.upper()
    @staticmethod
    def reversed(text):
        return text[::-1]
str_format = StringFormat()
print(str_format.first("Python"))
print(str_format.last("Python"))
print(str_format.lower("Python"))
print(str_format.upper("Python"))
print(str_format.reversed("Python"))