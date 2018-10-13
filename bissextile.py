#!/usr/bin/python
# -*-coding: utf-8 -*

import os
annee = input("Saisissez une année :\n")
try:
	annee = int(annee)
	assert annee > 0
except ValueError:
	print("Vous n'avez pas saisis un nombre.")
except AssertionError:
	print("L'année saisie est supérieure ou égale à 0.")
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
	print("Cette année est bissextile !")
else:
	print("Cette année n'est pas bissextile !")
os.system("pause")
