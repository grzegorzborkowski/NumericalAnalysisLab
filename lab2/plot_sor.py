import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def plot_zad_3_norma_od_rozmiaru():
    data = np.loadtxt('testssor/norma_rozmiar1.txt')
    plt.plot(data[:,0], data[:,1], 'ro')
    plt.xlabel('Rozmiar maceirzy', fontsize=50)
    plt.ylabel('Norma wyniku', fontsize=50)
    matplotlib.rcParams.update({'font.size': 22})

    data2 = np.loadtxt('testssor/norma_rozmiar2.txt')
    plt.plot(data2[:,0], data2[:,1], 'bo')
    plt.show()


def plot_zad3_norma_od_relaksacji():
    data = np.loadtxt('testssor/norma_relaksu1.txt')
    plt.plot(data[:,0], data[:,1], 'ro')
    plt.xlabel('Parametr relaksacji', fontsize=50)
    plt.ylabel('Norma wyniku', fontsize=50)
    matplotlib.rcParams.update({'font.size': 22})

    data2 = np.loadtxt('testssor/norma_relaksu2.txt')
    plt.plot(data2[:,0], data2[:,1], 'bo')
    plt.show()

def plot_zad3_iteracje_od_relaksacji():
    data = np.loadtxt('testssor/norma_relaksu1.txt')
    plt.semilogy(data[:,0], data[:,2], 'ro')
    plt.xlabel('Parametr relaksacji', fontsize=50)
    plt.ylabel('Liczba iteracji', fontsize=50)
    matplotlib.rcParams.update({'font.size': 22})

    data2 = np.loadtxt('testssor/norma_relaksu2.txt')
    plt.plot(data2[:,0], data2[:,2], 'bo')
    plt.show()

def plot_zad3_iteracje_od_wektorapoczatkowego():
    data = np.loadtxt('testssor/iteracje_poczatku1.txt')
    plt.plot(data[:,0], data[:,1], 'ro')
    plt.ylim([22,40])
    plt.xlabel('Wektor poczatkowy', fontsize=50)
    plt.ylabel('Liczba iteracji', fontsize=50)
    matplotlib.rcParams.update({'font.size': 22})

    data2 = np.loadtxt('testssor/iteracje_poczatku2.txt')
    plt.plot(data2[:,0], data2[:,1], 'bo')
    plt.show()

def plot_zad3_iteracje_od_ro():
    data = np.loadtxt('testssor/iteracje_ro1.txt')
    plt.plot(data[:,0], data[:,1], 'ro')
    plt.xlim([-0.001, 0.08])
    plt.xlabel('Wartosc ro', fontsize=50)
    plt.ylabel('Liczba iteracji', fontsize=50)
    matplotlib.rcParams.update({'font.size': 22})

    data2 = np.loadtxt('testssor/iteracje_ro2.txt')
    plt.plot(data2[:,0], data2[:,1], 'bo')
    plt.show()

plot_zad3_iteracje_od_ro()