from lab3 import functions


def first_criterion(x1, x2, stop_value):
    return abs(x1-x2) < stop_value


def second_criterion(x, fun, n, m, stop_value):
    return abs(fun(x, n, m)) < stop_value


def derivative(f, n, m):
    def compute(x, dx=0.00001):
        return (f(x+dx, n, m) - f(x, n, m)) / dx
    return compute


def newton(x1, fun, n=None, m=None, stop_criterion=None, stop_value=None):
    if stop_criterion is None:
        stop_criterion = 1

    if stop_value is None:
        stop_value = 0.00001

    if n is None:
        n = 10

    if m is None:
        m = 50

    iteration = 0
    df = functions.derivative_function

    while True:
        x2 = x1 - fun(x1, n, m) / df(x1)
        if stop_criterion == 1:
            value = first_criterion(x1, x2, stop_value)
            if value:
                break
        if stop_criterion == 2:
            value = second_criterion(x2, fun, n, m, stop_value)
            if value:
                break
        x1 = x2
        iteration += 1

    return iteration, x1


def euler(a, b, fun, n=None, m=None, stop_criterion=None, stop_value=None):
    if stop_criterion is None:
        stop_criterion = 1

    if stop_value is None:
        stop_value = 0.00001

    if n is None:
        n = 10

    if m is None:
        m = 50

    iteration = 0
    x0 = a
    x1 = b
    while True:
        fun_dif = fun(x1, n, m) - fun(x0, n, m)
        if fun_dif == 0:
            return -1
        x2 = x1 - fun(x1, n, m)*(x1-x0)/fun_dif

        if stop_criterion == 1:
            value = first_criterion(x1, x2, stop_value)
            if value:
                break

        if stop_criterion == 2:
            value = second_criterion(x2, fun, n, m,  stop_value)
            if value:
                break

        x0 = x1
        x1 = x2
        iteration += 1

    return iteration, x1

