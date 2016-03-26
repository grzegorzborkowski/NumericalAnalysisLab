from numpy import *
from jacob import *

def generate_tests_promien_spektralny():
    with open('tests/promien_spektralny.txt', 'a+') as f:
        for i in range(2, 20, 1):
            A = fill_matrix(i, k=10, m=1)
            promien_spektralny_value = oblicz_promien_spektralny(A)
            f.write(str(i))
            f.write(" ")
            f.write(str(promien_spektralny_value))
            f.write("\n")
        for i in range(20,1000,10):
            A = fill_matrix(i, k=10, m=1)
            promien_spektralny_value = oblicz_promien_spektralny(A)
            f.write(str(i))
            f.write(" ")
            f.write(str(promien_spektralny_value))
            f.write("\n")

def generate_tests_for_size_of_array():
    for k in [1,2]:
        file_name = 'tests/matrix_size' + str(k) + '.txt'
        with open(file_name, 'a+') as f:
            f.write("Rozmiar macierzy, norma z roznicy, ilosc iteracji, promien spektralny")
            for i in range(2, 20, 1):
                A = fill_matrix(i, k=10, m=1)
                guess = generate_x_vector(A)
                B = calculate_output_vector(A, guess)
                sol, iteration = jacobi(A, B, initial_guess=None, stopcriterium=0.00001, whichstopcriterium=k)
                norm = calculate_solution_norm(guess, sol)
                f.write(str(len(A[0])))
                f.write(" ")
                f.write(str(norm))
                f.write(" ")
                f.write(str(iteration))
                f.write("\n")
            for i in range(20, 1000, 10):
                A = fill_matrix(i, k=10, m=1)
                guess = generate_x_vector(A)
                B = calculate_output_vector(A, guess)
                sol, iteration = jacobi(A, B, initial_guess=None, stopcriterium=0.00001, whichstopcriterium=k)
                norm = calculate_solution_norm(guess, sol)
                f.write(str(len(A[0])))
                f.write(" ")
                f.write(str(norm))
                f.write(" ")
                f.write(str(iteration))
                f.write("\n")

def generate_tests_for_stop_criterium():
    for k in [1,2]:
        file_name = 'tests/ro_value' + str(k) + '.txt'
        with open(file_name, 'a+') as f:
            x = 0.000000001
            A = fill_matrix(100, k=10, m=1)
            guess = generate_x_vector(A)
            B = calculate_output_vector(A, guess)
            while(x < 0.1):
                sol, iteration = jacobi(A, B, initial_guess=None, stopcriterium=x, whichstopcriterium=k)
                norm = calculate_solution_norm(guess, sol)
                f.write(str(norm))
                f.write(" ")
                f.write(str(x))
                f.write("\n")
                x *= 2

def generate_tests_for_initial_vector():
    for k in [1,2]:
        file_name = 'tests/init_value' + str(k) + '.txt'
        with open(file_name, 'a+') as f:
            x_value = 1000
            A = fill_matrix(100, k=10, m=1)
            guess = generate_x_vector(A)
            B = calculate_output_vector(A, guess)
            while(x_value != -10):
                x = full(len(A[0]), x_value)
                sol, iteration = jacobi(A, B, initial_guess=x, stopcriterium=0.00001, whichstopcriterium=k)
                f.write(str(x_value))
                f.write(" ")
                f.write(str(iteration))
                f.write("\n")
                x_value -= 10

def generate_tests_for_iteration_number_from_ro():
    for k in [1,2]:
        file_name = 'tests/ro_value_iteration' + str(k) + '.txt'
        with open(file_name, 'a+') as f:
            x = 0.000000001
            A = fill_matrix(100, k=10, m=1)
            guess = generate_x_vector(A)
            B = calculate_output_vector(A, guess)
            while(x < 0.1):
                sol, iteration = jacobi(A, B, initial_guess=None, stopcriterium=x, whichstopcriterium=k)
                f.write(str(x))
                f.write(" ")
                f.write(str(iteration))
                f.write("\n")
                x *= 2

generate_tests_promien_spektralny()