#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from math import sqrt
import utilitaires

a = input("Entrez le 1er coefficient a : ")
b = input("Entrez le 2e coefficient b : ")
c = input("Entrez le 3  coefficient c : ")
a,b,c = int(a),int(b),int(c)
if a == 0:
    if b == 0:
        if c == 0:
            print("La solution est S = |R ")
        else:
            print("S = { }")
    else:
        print("La solution est S = { ",-c/b," }")
else:
    d = b*b - 4*a*c
    if d < 0:
        print("La solution est S = { } ")
    elif d == 0:
        print("La solution est S = {",-b/2*a,"}")
    else:
        print("Cette équation a deux solutions : S = { ",(-b-sqrt(d))/2*a," ; ",(-b+sqrt(d))/2*a, " }")

os.system("pause")
