import numpy
from numpy.linalg import inv


def calculate_jacobian_in_point(x1, x2,x3):
    jacobian = numpy.zeros((3,3))
    jacobian[0][0] = 2*x1
    jacobian[0][1] = 2*x2
    jacobian[0][2] = 1
    jacobian[1][0] = 4*x1
    jacobian[1][1] = 2*x2
    jacobian[1][2] = 3*pow(x3,2)
    jacobian[2][0] = 3
    jacobian[2][1] = -6*pow(x2,2)
    jacobian[2][2] = -4*x3
    return jacobian


def calculate_function_in_point(x1,x2,x3):
    function_vector = numpy.zeros((3,1))
    function_vector[0] = pow(x1,2)+pow(x2,2)+x3-1
    function_vector[1] = 2*pow(x1,2)+pow(x2,2)+pow(x3,3)-2
    function_vector[2] = 3*x1 - 2*pow(x2,3)-2*pow(x3,2)-3
    return function_vector


def solve_equations_system(stop_criterion, stop_value, x):
    initial_vector = numpy.ones((3,1))
    initial_vector[0] = x
    initial_vector[1] = x
    initial_vector[2] = x

    iteration = 0

    while True:
        inverted_matrix = inv(calculate_jacobian_in_point(initial_vector[0], initial_vector[1], initial_vector[2]))
        function_vector = calculate_function_in_point(initial_vector[0], initial_vector[1], initial_vector[2])
        delta = numpy.dot(inverted_matrix, function_vector)
        initial_vector -= delta
        iteration += 1
        if stop_criterion == 1:
            if abs(delta[0]) < stop_value and abs(delta[1]) < stop_value and abs(delta[2]) < stop_value:
                break

        if stop_criterion == 2:
            if abs(function_vector[0]) < stop_value and abs(function_vector[1]) < stop_value and abs(function_vector[2]) < stop_value:
                break

    return initial_vector, iteration


def generate_tests_for_equations_system():
        initial_stop_value = 0.00000001
        ending_stop_value = 1
        for x in numpy.arange (-10, 10, 0.1):
            for k in [1,2]:
                stop_value = initial_stop_value
                file_name = "tests/equations_XOXOXO" + str(k) + ".txt"
                with open(file_name, 'a+') as f:
                    while stop_value < ending_stop_value:
                        solution, iteration = solve_equations_system(k, stop_value, x)
                        f.write('%s %s %s %s \n' % (stop_value, solution, x, iteration))
                        stop_value *= 2

generate_tests_for_equations_system()