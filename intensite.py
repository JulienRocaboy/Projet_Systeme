#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, subprocess, sys, os
import matplotlib.pyplot as plt

repo = os.getcwd() # Vérification de présence du fichier txt
liste_fichier = os.listdir(repo)
if "Spc_photo.txt" not in liste_fichier:
    raise FileNotFoundError("Il manque le fichier txt")

if len(sys.argv)>1:  # Vérif de présence de l'argument
    inter=int(sys.argv[1])
else:
    inter=10


rep = {}
spc=open('Spc_photo.txt')
inte=[]
long=[]
inte_t=[]
long_t=[]
i=0
nb = re.compile(r"^(\d+\.\d+)\s+(-?\d+\.\d)") # recherche de motif "nombre.nombre nombre.nombre"

mini = None

for ligne in spc:  # Calcul de la borne minimum
    x = nb.match(ligne)
    if x:
        mini = int(float(x.group(1)))
        break

if mini is None:
    raise ValueError("Aucune valeur numérique trouvée")

spc.seek(0) #replace la lecture au début
maxi = mini + inter

for ligne in spc:
    x = nb.match(ligne)
    if x :
        longueur_onde = float(x.group(1))
        intensite = float(x.group(2))
        if longueur_onde<maxi:
            i+=1
            inte.append(intensite)
            long.append(longueur_onde)
            inte_t.append(intensite)
            long_t.append(longueur_onde)
        else:
            rep[mini,maxi] = inte,long,i,min(inte),sum(inte)/len(inte),max(inte)
            i=1
            mini += 10
            maxi += 10
            inte=[]
            long=[]
            inte.append(intensite)
            long.append(longueur_onde)
    if len(inte)>1 and not x: # Pour la fin des valeurs
            rep[mini,maxi] = inte,long,i,min(inte),sum(inte)/len(inte),max(inte)
            inte.append(intensite)
            long.append(longueur_onde)

if __name__ == "__main__":    #empeche de ploter deux fois
    plt.plot(long_t, inte_t)
    plt.ylabel('Intensité')
    plt.xlabel("Longueur d'onde")
    plt.grid('both')
    plt.show()

    print(rep.keys())