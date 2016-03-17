# Uklad a) k=10, m=1 <- zad indywidualne

from pprint import pprint
from numpy import array, ones, zeros, diag, diagflat, dot, linalg, fromfunction, random
from numpy import *


def jacobi(A, b, N=25, initial_guess=None, stopcriterium=None):
    if stopcriterium is None:
        stopcriterium = 0.00001

    if initial_guess is None:
        initial_guess = zeros(len(A[0]))

    D = diag(A)
    R = A - diagflat(D)

    x = initial_guess
    # Iterate for N times
    var = 1 # used for infinite loop
    iteration = 0
    while var == 1:
        iteration += 1
        y = x
        x = (b - dot(R,x)) / D
        #if stopcriterium and linalg.norm(y - x) < stopcriterium:
        #    break
        if stopcriterium and linalg.norm(dot(A, x)-b) < stopcriterium:
            break

    return x, iteration


def fill_matrix(N, k, m):
    A = fromfunction(lambda i, j: m / (N- i- j + 0.5), (N,N))
    for h in range(N):
        A[h][h] = k
    return A


def generate_x_vector(A):
    x = random.random_integers(-1, 1, len(A[0]))
    for i in range(len(A[0])):
        if x[i] == 0:
            x[i] = -1
    return x


def calculate_output_vector(A, x):
    return dot(A, x)


def calculate_solution_norm(x, sol):
    return linalg.norm(x-sol)

#A = fill_matrix(100, k=10, m=1)
#guess = generate_x_vector(A)
#B = calculate_output_vector(A, guess)

#print(A)
#print(guess)
#print(B)
#sol, iteration = jacobi(A, B, 25, None, 0.00001)
#print(sol)
#norm = calculate_solution_norm(guess, sol)

for i in range(2, 2000, 10):
    A = fill_matrix(i, k=10, m=1)
    guess = generate_x_vector(A)
    B = calculate_output_vector(A, guess)
    sol, iteration = jacobi(A, B, 25, None, 0.00001)
    norm = calculate_solution_norm(guess, sol)
    print(len(A[0]))
    print(norm)
    print(iteration)
    print("-----------")
