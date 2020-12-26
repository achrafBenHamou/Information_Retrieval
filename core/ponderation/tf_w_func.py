from math import log

def b(tf):
    if tf:
        return 1
    return 0


def n(tf):
    if tf:
        return tf
    else:
        return 0


def m(tf, maxt_prime):
    return tf / (maxt_prime + 0.00001)


def a(tf, maxt_prime):
    return 0.5 + 0.5 * (tf / (maxt_prime + 0.000001))


def s(tf):
    return tf ** 2


def l(tf):
    return 1 + log(tf)


def frac(tf):
    pass


def singhal(tf):
    pass
