from lab3 import numeric_functions
from lab3 import functions


def execute_newton_and_euler_tests(f, a, b, fun, k, ro, n=None, m=None):
    x = a+0.1
    while x < b:
        iteration_newton, solution_newton = numeric_functions.newton(x, fun, n, m, stop_criterion=k, stop_value=ro)
        iteration_euler = numeric_functions.euler(a, x, fun, n, m, stop_criterion=k, stop_value=ro)
        print(iteration_euler)
        f.write('%s %s %s %s %s %s \n' % (a, x, ro, iteration_euler, iteration_newton, solution_newton))
        x += 0.1


def numeric_tests(a, b, fun, initial_stop_value=None, ending_stop_value=None):
    if initial_stop_value is None:
        initial_stop_value = 0.00001

    if ending_stop_value is None:
        ending_stop_value = 1

    for k in [1, 2]:
        file_name = "tests/iterations_total_euler_next" + str(k) + ".txt"
        with open(file_name, 'a+') as f:
            ro = initial_stop_value
            while ro < ending_stop_value:
                execute_newton_and_euler_tests(f, a, b, fun, k, ro, n=None, m=None)
                ro *= 2


numeric_tests(-0.5, 1.5, functions.given_function, initial_stop_value=None, ending_stop_value=None)

