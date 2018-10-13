#!/usr/bin/python
# -*-coding: utf-8 -*

"""module multipli contenant la fonction table"""

import os

def table(nb,max=12):
    """Fonction affichant la table de multiplication par nb de 1*nb a max*nb (max >= 0)"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

# test de la fonction table
if __name__ == "__main__":
    table(5, 20)
    os.system("pause")
    
