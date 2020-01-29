import random


def gen_passwords(ch, ln, num):
    return [''.join(random.choice(ch) for _ in range(ln)) for _ in range(num)]
