#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import matplotlib.pyplot as plt
from intensite import rep



interv1=int(input("Borne inférieur : "))

donnees = [] #liste pour récupérer les données qui nous intérresse
donnees = rep[interv1, interv1+10]
print(donnees[2:10]) 

intensite=donnees[0]
longueur_onde=donnees[1]

#print(longueur_onde)

plt.plot(longueur_onde, intensite)
plt.show()