#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import matplotlib.pyplot as plt

spc = open("Spc_photo.txt")
inter1=input("Rentrer une longueur d'onde minimum : ")
inter2=input("Rentrer une longueur d'onde minimum : ")
longueur_onde=[]
intensite=[]
nb = re.compile(r"^(\d+\.\d+)\s+(-?\d+\.\d)")

for ligne in spc:
    x = nb.match(ligne)
    if x:
        if x.group(1) >= inter1 and x.group(1)<= inter2:
            lo = float(x.group(1))
            inte = float(x.group(2))
            longueur_onde.append(lo)
            intensite.append(inte)

plt.plot(longueur_onde, intensite)
plt.show()