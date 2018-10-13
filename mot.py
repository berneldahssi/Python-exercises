#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
mot = input("Entrez un mot : ")
mot = mot.lower()
longueurMot = len(mot)
def voyelles(mot):
    voyelles = 0
    for i in mot:
        if i in "aeiouy":
            voyelles += 1
    return voyelles
def envers(mot):
    motEnvers = ""
    i = 0
    while i < longueurMot:
        motEnvers = mot[i] + motEnvers
        i += 1
    return motEnvers
def leetLanguage(mot):
    motLeetLanguage = ""
    i = 0
    while i < longueurMot:
        if mot[i] == "a":
            lettres = "4"
        elif mot[i] == "b":
            lettres = "8"
        elif mot[i] == "c":
            lettres = "<"
        elif mot[i] == "d":
            lettres = "?"
        elif mot[i] == "e":
            lettres = "3"
        elif mot[i] == "f":
            lettres = "|="
        elif mot[i] == "g":
            lettres = "6"
        elif mot[i] == "h":
            lettres = "#"
        elif mot[i] == "k":
            lettres = "X"
        elif mot[i] == "l":
            lettres = "1_"
        elif mot[i] == "m":
            lettres = "^^"
        elif mot[i] == "n":
            lettres = "//"
        elif mot[i] == "o":
            lettres = "0"
        elif mot[i] == "p":
            lettres = "9"
        elif mot[i] == "q":
            lettres = "0."
        elif mot[i] == "r":
            lettres = "/2"
        elif mot[i] == "s":
            lettres = "5"
        elif mot[i] == "t":
            lettres = "7"
        elif mot[i] == "u":
            lettres = "(_)"
        elif mot[i] == "v":
            lettres = "1/"
        elif mot[i] == "w":
            lettres = "III"
        elif mot[i] == "x":
            lettres = "}{"
        elif mot[i] == "y":
            lettres = "j"
        elif mot[i] == "z":
            lettres = "2"
        motLeetLanguage = motLeetLanguage + lettres
        i += 1
    return motLeetLanguage
motLeetLanguage = leetLanguage(mot)
motEnvers = envers(mot)
nbVoyelles = voyelles(mot)
nbConsonnes = longueurMot - nbVoyelles
print("Ce mot a ",longueurMot," caractère(s)")
print("Ce mot compte ",nbVoyelles," voyelle(s) et ",nbConsonnes,"consonne(s)")
print("Ce mot en majuscule s'écrit : ",mot.upper())
print("Ce mot en minuscule s'écrit : ",mot)
print("Il s'écrit en l'envers : ",envers(mot))
if motEnvers == mot:
    print("Ce mot est un palindrome")
else:
    print("Ce mot n'est pas un palindrome")
print("Sa traduction en Leet Language donne : ",motLeetLanguage)
os.system("pause")
