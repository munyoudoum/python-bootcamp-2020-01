class Greeting:
    @staticmethod
    def say_hello():
        return "Hello!"
    @staticmethod
    def say_thanks():
        return "Thanks!"
    @staticmethod
    def say_goodbye():
        return "Good Bye!"

greeting = Greeting()
print(greeting.say_hello())
print(greeting.say_thanks())
print(greeting.say_goodbye())