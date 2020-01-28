import itertools


def all_passwords(ch, l):
    return sorted([''.join(p) for p in itertools.product(set(ch), repeat=l)])
