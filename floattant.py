#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def flottant(x):
    """Fonction prenant en paramètre un flottant et renvoyant une
chaîne de caractères représentant la troncature de ce nombre. La
partie flottante doit avoir une longueur maximum de 3 caractères.
De plus, on va remplacer le point décimal par la virgule"""

    if type(x) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    x = str(x)
    partie_entiere, partie_flottante = x.split(".")
    return ",".join([partie_entiere, partie_flottante[:3]])

if __name__ == "__main__":
    x = input("Entrez un flottant : ")
    print(flottant(x))

os.system("pause")
