#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from random import randrange
from math import ceil

def couleurCase(n):
    if n % 2 == 0:
        return ("noire")
    else:
        return ("rouge")

nGagnant = randrange(50)
argent = 1000
continuer_partie = True

prenom = input("Entrez votre prénom :  ")
print("\nBienvenu au Casino",prenom,"! \n\nMisez sur un numéro (compris entre 0 et 49)\
\net gagnez ou perdez de l'argent : telle est la fortune, au casino !\
\nVous vous installez à la table de roulette avec", argent,"$.")


while continuer_partie:

    nMise = -1
    while (nMise < 0 or nMise > 49):
        nMise = input("\nEntrez le numéro sur lequel vous souhaitez placer votre mise :  ")
        try:
            nMise = int(nMise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            nMise = -1
            continue
        if nMise < 0:
            print("Ce nombre est négatif")
        if nMise > 49:
            print("Ce nombre est supérieur à 49")
    print("\nLa case de votre numéro est de couleur",couleurCase(nMise))

    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("\nTapez le montant de votre mise (en $) :  ")
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est négative ou nulle")
        if mise > argent:
            print("Vous ne pouvez miser autant, vous n'avez que :", argent,"$" )

    nGagnant = randrange(50)
    print("\nLa roulette tourne... ... et s'arrête sur la case de numéro", nGagnant, "de couleur",couleurCase(nGagnant))
    if nMise == nGagnant:
        print("\n\nFélicitations", prenom,"!, vous gagnez", mise * 3,"$")
        argent += mise * 3
    elif couleurCase(nGagnant) == couleurCase(nMise):
        print("\n\nVous avez misé sur la bonne couleur", prenom,", vous gagnez", ceil(mise * 0.5),"$")
        argent += ceil(mise * 0.5)
    else:
        print("\n\nDésolé", prenom,", c'est pas pour cette fois. Vous perdez votre mise!")
        argent -= mise

    if argent <= 0:
        print("\nVous êtes ruiné", prenom," ! C'est la fin de la partie")
        continuer_partie = False
    else:
        print("Vous avez à présent :", argent, "$")
        quitter = input("Souhaitez-vous quitter le casino (Oui/Non) ?   ")
        if quitter == "oui" or quitter == "Oui":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False

os.system("pause")
