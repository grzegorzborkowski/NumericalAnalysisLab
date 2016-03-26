from numpy import linalg, copy, dot, zeros


def sor(A, b, initial_guess=None, factor=None, stop_criterium=None, which_stopcriterium=None):
    """
   Successive over-relaxation method
   """
    n = len(A[0])
    if initial_guess is None:
        initial_guess = zeros(n)

    if stop_criterium is None:
        stop_criterium = 0.00001

    if which_stopcriterium is None:
        which_stopcriterium = 1

    if factor is None:
        factor = 1.5

    iteration = 0
    x = initial_guess
    while True:
        y = copy(x)
        iteration += 1
        for i in range(n):
            p = 0
            for j in range(n):
                if i != j:
                    p += A[i][j]*x[j]
            x[i] = (1-factor)*x[i] + (factor/A[i][i])*(b[i] - p)

        if stop_criterium and which_stopcriterium==1 and linalg.norm(y-x) < stop_criterium:
            break

        if stop_criterium and which_stopcriterium==2 and linalg.norm(dot(A, x)-b) < stop_criterium:
            break

    return x, iteration

