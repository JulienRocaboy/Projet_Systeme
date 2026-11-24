#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, subprocess, sys
import matplotlib.pyplot as plt

rep = {}
inter=10
#inter = int(sys.argv[1])
mini = 339
maxi = 339+inter
spc = open("Spc_photo.txt")
inte=[]
long=[]
inte_t=[]
long_t=[]
i=0
nb = re.compile(r"^(\d+\.\d+)\s+(-?\d+\.\d)")

for ligne in spc:
    x = nb.match(ligne)
    if x:
        longueur_onde = float(x.group(1))
        intensite = float(x.group(2))
        if longueur_onde<maxi:
            i+=1
            inte.append(intensite)
            long.append(longueur_onde)
            inte_t.append(intensite)
            long_t.append(longueur_onde)
        else:
            rep[mini,maxi] = inte,long,"Nombre d'intensité : ",i,"Intensité min : ",min(inte),"Intensité moyenne : ",sum(inte)/len(inte),"Intensité max", max(inte)
            i=1
            mini += 10
            maxi += 10
            inte=[]
            long=[]
            inte.append(intensite)
            long.append(longueur_onde)

if __name__ == "__main__":    #empeche de ploter deux fois
    plt.plot(long_t, inte_t)
    plt.show()
    print(rep.keys())