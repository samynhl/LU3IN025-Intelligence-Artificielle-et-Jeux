# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:07:05 2022

@author: PC
"""
from fonctions import lirePrefEtd, lirePrefSpe, Algo1, Algo2, print_algo1, print_algo2


def main():
    PrefEtu = lirePrefEtd("./PrefEtu.txt")
    capacite, PrefSpe = lirePrefSpe("./PrefSpe.txt")
    print_algo1(Algo1(PrefEtu, PrefSpe, capacite)[0])

    PrefEtu = lirePrefEtd("./PrefEtu.txt")
    capacite, PrefSpe = lirePrefSpe("./PrefSpe.txt")
    print_algo2(Algo2(PrefEtu, PrefSpe, capacite))


main()