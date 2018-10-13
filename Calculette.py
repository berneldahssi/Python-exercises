#!/usr/bin/python
# -*-coding: utf-8 -*

import os
print("On représente les types d'opération par les chiffres :\n1: Addition          2: Soustraction\n3: Multiplication    4: Division\n")
replay = True
while replay:
	operation = input("Entrez le chiffre correspondant au type d'opérations que vous souhaitez effectuer :  ")
	try:
		operation = int(operation)
	except ValueError:
		print("Vous n'avez pas saisi un chiffre")
		continue
	if operation == 1 or operation == 2 or operation == 3 or operation == 4:
		n1 = input("Entrez le premier nombre\n")
		n2 = input("Entrez le second nombre\n")
		n1,n2 = int(n1),int(n2)
		if operation == 1:
			n = n1 + n2
		if operation == 2:
			n = n1 - n2
		if operation == 3:
			n = n1 * n2
		if operation == 4:
			n = n1 / n2
		print("Votre résultat est :",n)
	else:
		print("Ce chiffre ne figure pas dans la liste des chiffres proposés plus haut !!!")
		continue
	autre = input("Voulez-vous effectuer une autre opération ? O : Oui ou N : Non\n")
	if autre.lower() == "oui" or "o":
		replay = True
print("Merci d'avoir utilisé BG_calculette")
os.system("pause")
