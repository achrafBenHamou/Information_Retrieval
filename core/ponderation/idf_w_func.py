from math import log


def n():
    return 1


def t(length_d, df):
    return log(length_d / df)


def MG(length_d, df):
    return log(1 + length_d / df)


def f(df):
    return 1 / df


def p(length_d, df):
    return log((length_d - df) / df)


def MG_bis(maxt_prime, df):
    return log(1 + (maxt_prime / df))


def s(length_d, df):
    return log((length_d + 1) / df)**2


