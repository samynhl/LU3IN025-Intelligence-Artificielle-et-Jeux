# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:58:27 2022

@author: PC
"""
from fonctions import plot_complexity

def complexity_gs():
    ITER = 2000; INIT = 200; pas = 200; p = 9

    iters = plot_complexity(INIT, ITER, p, pas, 0)

    iters = plot_complexity(INIT, ITER, p, pas, 1)

    print("\nLa valeur moyenne des itérations : ", sum(iters)/len(iters))

complexity_gs()
