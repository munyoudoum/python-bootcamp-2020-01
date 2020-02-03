import random


class Bot():
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return "My name is {}! I am a BOT!".format(self.name)

    def good_luck(self, newname):
        self.newname = newname
        return f"Nice to meet you {self.newname}! Good luck for the Bootcamp!"

    def random_quote(self):
        res = ["Making mistakes is better than faking perfection."]
        res.append("Creativity takes courage.")
        res.append("Your limitation is only your imagination.")
        return random.choice(res)
bot = Bot("srfdsf")
print(bot.introduce())
print(bot.good_luck("s"))
print(bot.random_quote())
print(bot.random_quote())
print(bot.random_quote())