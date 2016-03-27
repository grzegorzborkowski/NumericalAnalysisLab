import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def plot_charts_first_criterion():
    data = np.loadtxt('tests/iterations1.txt')
    plt.plot(data[:, 0], data[:, 1], 'ro')
    plt.xlabel("Warunek stopu", fontsize=50)
    plt.ylabel("Liczba iteracji", fontsize=50)
    matplotlib.rcParams.update({'font.size': 22})
    plt.plot(data[:, 0], data[:, 2], 'bo')
    plt.show()

plot_charts_first_criterion()