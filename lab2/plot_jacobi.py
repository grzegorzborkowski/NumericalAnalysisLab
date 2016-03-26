import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import matplotlib


def plot_zad1_different_matrix_size_norma_wyniku_pierwsze_kryterium():
    #Rozmiar macierzy, norma z roznicy, ilosc iteracji, promien spektralny
    data = np.loadtxt('tests/matrix_size1.txt')

    pl.plot(data[:,0], data[:,1], 'ro')
    plt.xlabel('Rozmiar macierzy', fontsize=50)
    plt.ylabel('Norma wyniku', fontsize=50)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    matplotlib.rcParams.update({'font.size': 22})

    pl.show()


def plot_zad1_different_matrix_size_norma_wyniku_drugie_kryterium():
    #Rozmiar macierzy, norma z roznicy, ilosc iteracji, promien spektralny
    data = np.loadtxt('tests/matrix_size2.txt')

    pl.plot(data[:,0], data[:,1], 'ro')
    plt.xlabel('Rozmiar macierzy', fontsize=50)
    plt.ylabel('Norma wyniku', fontsize=50)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    matplotlib.rcParams.update({'font.size': 22})

    pl.show()


def plot_zad1_norma_od_dokladnosci():
    data = np.loadtxt('tests/ro_value1.txt')

    pl.loglog(data[:,1], data[:,0], 'ro', basex=10)
    plt.xlabel('Stop', fontsize=50)
    plt.ylabel('Norma wyniku', fontsize=50)
    matplotlib.rcParams.update({'font.size': 22})

    pl.show()

def plot_zad1_norma_od_dokladnosci_2():
    data = np.loadtxt('tests/ro_value2.txt')

    pl.loglog(data[:,1], data[:,0], 'ro', basex=10)
    plt.xlabel('Stop', fontsize=50)
    plt.ylabel('Norma wyniku', fontsize=50)
    matplotlib.rcParams.update({'font.size': 22})

    pl.show()

def plot_zad_liczba_iteracji_od_wektora_poczatkowego_1():
    data = np.loadtxt('tests/init_value1.txt')

    pl.plot(data[:,0], data[:,1], 'ro')
    pl.ylim([10,20])
    plt.xlabel('Składowa wektora', fontsize=50)
    plt.ylabel('Liczba iteracji', fontsize=50)
    matplotlib.rcParams.update({'font.size': 22})

    pl.show()


def plot_zad_liczba_iteracji_od_wektora_poczatkowego_2():
    data = np.loadtxt('tests/init_value2.txt')

    pl.plot(data[:,0], data[:,1], 'ro')
    pl.ylim([10,20])
    plt.xlabel('Składowa wektora', fontsize=50)
    plt.ylabel('Liczba iteracji', fontsize=50)
    matplotlib.rcParams.update({'font.size': 22})

    pl.show()


def plot_liczba_iteracji_od_wartosci_ro():
    data = np.loadtxt('tests/ro_value_iteration1.txt')

    plt.semilogx(data[:,0], data[:,1], 'ro')
    plt.ylim([5, 24])
    plt.xlabel('Wartosc ro', fontsize=50)
    plt.ylabel('Liczba iteracji', fontsize=50)
    matplotlib.rcParams.update({'font.size': 22})

    data2 = np.loadtxt('tests/ro_value_iteration2.txt')

    plt.semilogx(data2[:,0], data2[:,1], 'bo')
    pl.show()

def generate_tests_for_norm_from_initial_vector():
    data = np.loadtxt('tests/matrix_size1.txt')

    plt.semilogx(data[:,0], data[:,2], 'ro')
    plt.ylim([5, 24])
    plt.xlabel('Rozmiar macierzy', fontsize=50)
    plt.ylabel('Liczba iteracji', fontsize=50)
    matplotlib.rcParams.update({'font.size': 22})

    data2 = np.loadtxt('tests/matrix_size2.txt')

    plt.semilogx(data2[:,0], data2[:,2], 'bo')
    pl.show()

def plot_promien():
    data = np.loadtxt('tests/promien_spektralny.txt')
    pl.plot(data[:,0], data[:,1], 'ro')
    plt.xlabel('Rozmiar macierzy', fontsize=50)
    plt.ylabel('Promien spektralny', fontsize=50)
    matplotlib.rcParams.update({'font.size': 22})
    plt.show()

plot_promien()