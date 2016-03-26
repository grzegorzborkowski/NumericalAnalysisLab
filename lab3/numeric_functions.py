def first_criterion(x1, x2, stop_value):
    if abs(x1-x2) < stop_value:
        return True
    return False


def second_criterion(x, fun, stop_value):
    if abs(fun(x)) < stop_value:
        return True
    return False


def derivative(f):
    def compute(x, dx=0.00001):
        return (f(x+dx) - f(x)) / dx
    return compute


def newton(x1, fun, stop_criterion=None, stop_value=None):
    if stop_criterion is None:
        stop_criterion = 1

    if stop_value is None:
        stop_value = 1

    iteration = 0
    while True:
        x2 = x1 - fun(x1)/derivative(fun)
        if stop_criterion == 1:
            value = first_criterion(x1, x2, stop_value)
            if value:
                break
        if stop_criterion == 2:
            value = second_criterion(x2, fun, stop_value)
            if value:
                break
        x1 = x2
        iteration += 1

    return iteration


def euler(a, b, fun, stop_criterium=None, stop_value=None):
    if stop_criterium is None:
        stop_criterium = 1

    if stop_value is None:
        stop_value = 0.00001

