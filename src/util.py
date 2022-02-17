import numpy as np
import random
import time
import matplotlib.pyplot as plt
from fonctions import *

# Data structures
nom_parcours = {0: 'ANDROIDE', 1: 'BIM', 2: 'DAC', 3: 'IMA',
                4: 'RES', 5: 'SAR', 6: 'SESI', 7: 'SFPN', 8: 'STL'}


def lirePrefEtd(path):
    with open(path, "r") as f:
        lines = f.readlines()
        Pref_list = []
        for line in lines[1:]:
            Pref_list.append(line.split()[2:])
    return Pref_list


def lirePrefSpe(path):
    with open(path, "r") as f:
        lines = f.readlines()
        capacite = [int(x) for x in lines[1].split()[1:]]
        Pref_list = []
        for line in lines[2:]:
            liste = line.split()
            Pref_list.append(liste[2:])
    return capacite, Pref_list


def print_algo1(dic):
    print("Résultats de l'algorithme de Gale-Shapley coté Etudiant :\n")
    for k in dic.keys():
        print("\tEtudiant {} est affecté au parcours  :  {}".format(k, nom_parcours[dic[k]]))


def print_algo2(dic):
    print("\nRésultats de l'algorithme de Gale-Shapley coté Parcours :\n")
    for k in dic.keys():
        print("\tParcours {} : {}".format(nom_parcours[k], dic[k]))


def genererPrefEtu(n, p):
    PrefEtu = []
    for i in range(n):
        a = random.sample(range(0, p), p)
        b = [str(x) for x in a]
        PrefEtu.append(b)
    return PrefEtu


def genererPrefSpe(n, p):
    PrefSpe = []
    for i in range(p):
        a = random.sample(range(0, n), n)
        b = [str(x) for x in a]
        PrefSpe.append(b)
    return PrefSpe


def genererCapacite(n, p):
    r = n//5
    C = np.random.randint(1, r, p)
    s = sum(C)
    if s > n:
        k = 0
        while True:
            i = np.random.randint(0, p, 1)
            if C[i] > 1:
                C[i] -= 1
                k += 1
                if k > n-s:
                    break
    else:
        if s < n:
            for k in range(1, n-s+1):
                i = np.random.randint(0, p, 1)
                C[i] += 1
    return C
