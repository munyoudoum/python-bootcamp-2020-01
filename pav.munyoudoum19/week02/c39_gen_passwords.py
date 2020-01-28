import random


def gen_passwords(ch, l, num):
    return [''.join(random.choice(ch) for _ in range(l)) for _ in range(num)]
