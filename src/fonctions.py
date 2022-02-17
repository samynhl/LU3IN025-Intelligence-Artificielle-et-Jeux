# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:07:26 2022

@author: PC
"""

import time
import matplotlib.pyplot as plt
from util import *

# Algorithme Gale-Shapley coté étudiant


def Algo1(PrefEtu, PrefSpe, capacite):
    # Structures intermédiaires
    dicEtu = {}  # contiendra les couples etu-par
    dicSpe = {}  # contiendra les couples par-etu
    celib = []
    cpt = 0  # compteur du nombre d'itérations

    # Initialisation
    for i in range(len(PrefEtu)):
        dicEtu[i] = None
        celib.append(i)
    for i in range(len(PrefSpe)):
        dicSpe[i] = []

    # Boucle principale
    while celib:
        cpt += 1
        etu = celib[0]
        pref = int(PrefEtu[etu][0])
        PrefEtu[etu].pop(0)
        i1 = PrefSpe[pref].index(str(etu))
        if capacite[pref] > 0:  # Le parcours contient encore des places pédagogiques
            dicSpe[pref].append((i1, etu))
            # Garder la liste trié sur le classement dans le fichier de préférences
            dicSpe[pref].sort()
            dicEtu[etu] = pref
            capacite[pref] -= 1
            celib.pop(0)
        else:  # le parcours ne contient plus de places pédagogiques
            taille = len(dicSpe[pref])
            i2 = dicSpe[pref][taille-1][0]
            if i1 < i2:
                etu2 = int(dicSpe[pref][taille-1][1])
                dicSpe[pref].pop(taille-1)
                dicEtu[etu2] = None
                celib.append(etu2)
                dicSpe[pref].append((i1, etu))
                dicSpe[pref].sort()  # added
                dicEtu[etu] = pref
                celib.pop(0)
    return dicEtu, cpt

# Algorithme Gale-Shapley coté parcours


def Algo2(PrefEtu, PrefSpe, capacite):
    dicEtu = {}  # contiendra les couples etu-par
    dicSpe = {}  # contiendra les couples par-etu
    celib = []

    # Initialisation
    for i in range(len(PrefEtu)):
        dicEtu[i] = None
    for i in range(len(PrefSpe)):
        dicSpe[i] = []
        celib.append(i)
    # Boucle principale
    while celib:
        spec = celib[0]
        try:
            pref = int(PrefSpe[spec][0])
        except:
            print(spec)
            print(len(PrefSpe[spec]))
        PrefSpe[spec].pop(0)
        if dicEtu[pref] == None:  # l'étudiant n'est pas encore affecté
            dicSpe[spec].append(pref)
            dicEtu[pref] = spec
            capacite[spec] -= 1
            if (capacite[spec] == 0):
                celib.pop(0)
        else:  # l'étudiant est déja affecté à un parcours
            i1 = PrefEtu[pref].index(str(spec))
            i2 = PrefEtu[pref].index(str(dicEtu[pref]))
            if i1 < i2:
                if dicEtu[pref] not in celib:
                    celib.append(dicEtu[pref])
                dicSpe[spec].append(pref)
                dicSpe[int(dicEtu[pref])].remove(pref)
                capacite[int(dicEtu[pref])] += 1
                dicEtu[pref] = spec
                capacite[spec] -= 1
                if (capacite[spec] == 0):
                    celib.pop(0)
    return dicSpe


def plot_complexity(INIT, ITER, p, pas, type):
    elements = []
    times = []
    PrefEtu = []
    PrefSpe = []
    capacite = []
    iters = []
    a = 0
    b = 0
    for n in range(INIT, ITER+1, pas):
        for i in range(10):
            PrefEtu = genererPrefEtu(n, p)
            PrefSpe = genererPrefSpe(n, p)
            capacite = genererCapacite(n, p)
            start = time.time()
            dic, cpt = Algo1(PrefEtu, PrefSpe, capacite)
            end = time.time()
            a += end-start
            b += cpt
        iters.append(b/10)
        times.append(a/10)
        a = 0
        b = 0
        elements.append(n)

    plt.xlabel('Nombre etudiants')
    if type == 0:
        plt.ylabel('Complexité temporelle')
        label = "temps moyen en fonction de n"
        plt.plot(elements, times, label=label)
    else:
        if type == 1:
            plt.ylabel('Nombre itérations')
            label = "nombre iterations en fonction de n"
            plt.plot(elements, iters, label=label, c='r')
    plt.grid()
    plt.legend()
    plt.show()
    return iters
