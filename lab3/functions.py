from math import *


def function_a(x, n):
    return pow(x, n) - pow(1-x, n)


def function_b(x, n):
    return (x-1)*exp(-n*x) + pow(x, n)


def function_c(x, n):
    return pow(x, 2) - 4*pow(sin(x), n)


def function_d(x, n):
    return pow(x, n) + x


def function_e(x, n, m):
    return m*x*exp(-n) -m*exp(-n*x) + 1/m


