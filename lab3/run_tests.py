from lab3 import numeric_functions


def numeric_tests(a, b, fun, initial_stop_value=None, ending_stop_value=None):
    if initial_stop_value is None:
        initial_stop_value = 0.00001

    if ending_stop_value is None:
        ending_stop_value = 0.1

    for k in [1, 2]:
        file_name = 'iterations' + str(k) + '.txt'
        with open(file_name, 'a+') as f:
            ro = initial_stop_value
            while ro < ending_stop_value:
                x = b
                while x - a > 0:
                    iteration_newton = numeric_functions.newton(x, fun, k, ro)
                    iteration_euler = numeric_functions.euler(x, b, fun, k, ro)
                    f.write(str(ro))
                    f.write(" ")
                    f.write(str(iteration_newton))
                    f.write(" ")
                    f.write(str(iteration_euler))
                    f.write("\n")
                    x -= 0.1
            ro *= 2

