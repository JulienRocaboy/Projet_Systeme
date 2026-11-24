#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, subprocess, sys


rep = {}
#inter=10
inter = int(sys.argv[1])
fenetre1=int(sys.argv[2])
fenetre2=int(sys.argv[3])
mini = 339
maxi = 339+inter
spc = open("Spc_photo.txt")
inte=[]
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
        else:
            rep[mini,maxi] = "Nombre d'intensité : ",i,"Intensité min : ",min(inte),"Intensité moyenne : ",sum(inte)/len(inte),"Intensité max", max(inte)
            i=1
            mini += 10
            maxi += 10
            inte=[]
            inte.append(intensite)


print (rep[fenetre1,fenetre2])