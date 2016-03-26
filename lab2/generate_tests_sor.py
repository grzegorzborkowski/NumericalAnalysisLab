from sor import *
from jacob import *
from numpy import *

def zad3_norma_od_rozmiaru():
    def calculate():
        A = fill_matrix(i, k=10, m=1)
        guess = generate_x_vector(A)
        B = calculate_output_vector(A, guess)
        sol, _ = sor(A, B, initial_guess=None, factor=1.5, stop_criterium=None, which_stopcriterium=k)
        norm = calculate_solution_norm(guess, sol)
        f.write(str(len(A[0])))
        f.write(" ")
        f.write(str(norm))
        f.write(" ")
        f.write("\n")

    for k in [2]:
        file_name = 'testssor/norma_rozmiar' + str(k) + '.txt'
        with open(file_name, 'a+') as f:
            for i in range(2, 20, 1):
                calculate()
            for i in range(600, 620, 10):
                calculate()

def zad3_norma_od_relaksacji():
    def calculate(factor_value, k):
        A = fill_matrix(100, k=10, m=1)
        guess = generate_x_vector(A)
        B = calculate_output_vector(A, guess)
        sol, iteration = sor(A, B, initial_guess=None, factor=factor_value, stop_criterium=None, which_stopcriterium=k)
        norm = calculate_solution_norm(guess, sol)
        f.write(str(factor_value))
        f.write(" ")
        f.write(str(norm))
        f.write(" ")
        f.write(str(iteration))
        f.write(" ")
        f.write("\n")

    for k in [2]:
        factor_value = 1.001
        file_name = 'testssor/norma_relaksu' + str(k) + '.txt'
        with open(file_name, 'a+') as f:
            while(factor_value < 2):
                calculate(factor_value, k)
                factor_value += 0.001

def zad3_iteracje_od_poczatku():
    for k in [1,2]:
        file_name = 'testssor/iteracje_poczatku' + str(k) + '.txt'
        with open(file_name, 'a+') as f:
            x_value = 1000
            A = fill_matrix(100, k=10, m=1)
            guess = generate_x_vector(A)
            B = calculate_output_vector(A, guess)
            while(x_value != -10):
                x = full(len(A[0]), x_value)
                _, iteration = sor(A, B, x, factor=1.5, stop_criterium=None, which_stopcriterium=k)
                f.write(str(x_value))
                f.write(" ")
                f.write(str(iteration))
                f.write("\n")
                x_value -= 10

def zad3_iteracje_od_ro():
    for k in [1,2]:
        file_name = 'testssor/iteracje_ro' + str(k) + '.txt'
        with open(file_name, 'a+') as f:
            x = 0.000000001
            A = fill_matrix(100, k=10, m=1)
            guess = generate_x_vector(A)
            B = calculate_output_vector(A, guess)
            while (x < 0.1):
                _, iteration = sor(A, B, initial_guess=None, factor=1.5, stop_criterium=x, which_stopcriterium=k)
                f.write(str(x))
                f.write(" ")
                f.write(str(iteration))
                f.write("\n")
                x *= 2


zad3_iteracje_od_ro()