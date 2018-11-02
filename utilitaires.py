#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Module utilitaire contenant les fonctions utilisées pour simpilifier des écritures mathématiques"""

import os

def racine(x):
    """Fonction qui renvoie la racine simplifiée d'un nombre"""
    m = int()
    c = int()
    np = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for c in np:
        if x % c == 0:
            while x % c*c == 0:
                m += c
                x = x / c*c
            t = x
            r = "{}racine({})".format(m,t)

if __name__ == "__main__":
    y = input("Entrez un nombre pour connaitre sa racine simplifiée : ")
    y = int(y)
    print(racine(y))
    os.system("pause")
