#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, os
import matplotlib.pyplot as plt
from intensite import rep



interv1=int(input("Borne inférieur : "))


donnees = [] #liste pour récupérer les données qui nous intérresse
donnees = rep[interv1, interv1+10]
print("\n\nDonnées pour la fenêtre [", interv1,",",(interv1+10),"] :\n\n- Nombre d'intensité :",donnees[2],"\n- Intensité minimum :",donnees[3],"\n- Intensité moyenne :",donnees[4],"\n- Intensité maximum :",donnees[5]) # On print tout sauf les listes

intensite=donnees[0]
longueur_onde=donnees[1]

#print(longueur_onde)

plt.plot(longueur_onde, intensite)
plt.ylabel('Intensité')
plt.xlabel("Longueur d'onde")
plt.grid('both')
plt.show()