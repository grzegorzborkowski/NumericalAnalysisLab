from math import *


# https://www.wolframalpha.com/input/?i=50x*e%5E(-50)+-50*e%5E(-10*x)%2B1%2F500
def given_function(x, n=10, m=50):
    return m*x*exp(-m) - m*exp(-n*x) + 1/(n*m)


def derivative_function(x):
    return 50*(10*exp(-10*x)+1/(exp(50)))


