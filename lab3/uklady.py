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


def calculate_delta_p(x1,x2,x3):
    return numpy.linalg.solve(calculate_jacobian_in_point(x1,x2,x3), calculate_function_in_point(x1,x2,x3))


def check_if_is_solution(x1,x2,x3):
    return calculate_function_in_point(x1,x2,x3)


def solve_equations_system():
    initial_vector = numpy.ones((3,1))
    iteration = 0
    while True:
        inverted_matrix = inv(calculate_jacobian_in_point(initial_vector[0], initial_vector[1], initial_vector[2]))
        function_vector = calculate_function_in_point(initial_vector[0], initial_vector[1], initial_vector[2])
        delta = numpy.dot(inverted_matrix, function_vector)
        initial_vector -= delta
        iteration += 1
    return initial_vector, iteration


solution_vector, iteration = solve_equations_system()
print(check_if_is_solution(solution_vector[0], solution_vector[1], solution_vector[2]), iteration)