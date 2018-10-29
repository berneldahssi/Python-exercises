#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Module utilitaire contenant les fonctions utilisées pour simpilifier des écritures mathématiques"""

import os

def racine(x):
    """Fonction qui renvoie la racine simplifiée d'un nombre"""
    m = int()
    if x % 2 == 0:
        while x % 4 == 0:
            m += 2
            x = x / 4
        t = x
        r = "{}racine({})".format(m,t)
    if x % 3 == 0:
        while x % 9 == 0:
            m += 3
            x = x / 9
        t = x
        r = "{}racine({})".format(m,t)
    return r

if __name__ == "__main__":
    y = input("Entrez un nombre pour connaitre sa racine simplifiée : ")
    y = int(y)
    print(racine(y))
    os.system("pause")
