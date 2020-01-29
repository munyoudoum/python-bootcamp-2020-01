import itertools


def all_passwords(ch, ln):
    return sorted([''.join(p) for p in itertools.product(set(ch), repeat=ln)])
