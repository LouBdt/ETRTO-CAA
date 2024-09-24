#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:31:52 2024

@author: lou
"""
table_normes = [[7, 47, 93, ""], 
                [8, 47, 94, ""],
                [8, 50, 94, "200 x 50"],
                [8, 54, 110, ""],
                [8, 32, 137, ""],
                [10, 54, 152, ""],
                [10, 44, 194, ""],
                [11, 47, 222, ""],
                [12, 47, 203, ""],
                [12, 50, 203, ""],
                [12, 54, 203, ""],
                [12, 57, 203, ""],
                [12, 62, 203, "320 x 57"],
                [13, 67, 203, "330 x 65"],
                [12, 32, 239, "300 x 32A"],
                [12, 57, 239, "300 x 55A"],
                [12, 32, 248, "300 x 32A"],
                [12, 37, 248, ""],
                [14, 57, 251, "350 x 55R ou 315 x 55"],
                [14, 47, 254, ""],
                [14, 50, 254, ""],
                [14, 40, 279, "350 x 38B"],
                [14, 32, 288, "350 x 32"],
                [14, 37, 288, "350A ou 350 x 32A ou 350A Confort/Ballon"],
                [14, 40, 288, "350 x 38A"],
                [14, 47, 288, ""],
                [14, 32, 298, "350A ou 350 x 32A"],
                [14, 37, 298, "350 x 35A"],
                [14, 54, 298, ""],
                [16, 40, 305, ""],
                [16, 47, 305, ""],
                [16, 50, 305, ""],
                [16, 54, 305, ""],
                [16, 57, 305, ""],
                [16, 62, 305, ""],
                [16, 47, 317, ""],
                [16, 40, 330, "400 x 38B"],
                [16, 28, 340, "400 x 30A"],
                [16, 32, 340, "400A ou 400 x 32A"],
                [16, 37, 340, "400 x 35A ou 400A Confort/Ballon"],
                [16, 44, 340, ""],
                [16, 28, 349, ""],
                [16, 32, 349, "400 x 32A"],
                [16, 35, 349, ""],
                [16, 37, 349, ""],
                [16, 40, 349, ""],
                [17, 32, 357, ""],
                [17, 32, 369, ""],
                [17, 37, 369, ""],
                [18, 28, 355, ""],
                [18, 32, 355, ""],
                [18, 35, 355, ""],
                [18, 40, 355, ""],
                [18, 47, 355, ""],
                [18, 50, 355, ""],
                [18, 37, 387, ""],
                [18, 40, 387, ""],
                [18, 28, 390, "450 x 28A ou 450A"],
                [18, 32, 390, "450 x 32A ou 450A"],
                [18, 37, 390, "450 x 35A ou 450A Confort/Ballon"],
                [18, 55, 390, "450 x 55A"],
                [18, 57, 390, "450 x 55A ou 450A"],
                [18, 32, 400, "450 x 32A"],
                [18, 37, 400, ""],
                [20, 54, 400, "500 x 45"],
                [20, 67, 381, ""],
                [20, 28, 406, ""],
                [20, 32, 406, ""],
                [20, 35, 406, ""],
                [20, 37, 406, ""],
                [20, 40, 406, ""],
                [20, 42, 406, ""],
                [20, 44, 406, ""],
                [20, 47, 406, "500 x 45"],
                [20, 50, 406, ""],
                [20, 52, 406, ""],
                [20, 53, 406, ""],
                [20, 54, 406, ""],
                [20, 60, 406, ""],
                [20, 62, 406, ""],
                [20, 65, 406, ""],
                [20, 70, 406, ""],
                [20, 75, 406, ""],
                [20, 100, 406, ""],
                [20, 47, 419, ""],
                [20, 44, 428, ""],
                [20, 54, 428, ""],
                [20, 40, 432, ""],
                [20, 32, 438, "500 x 32 ANL"],
                [20, 37, 438, "500A"],
                [20, 40, 438, "500 x 38A"],
                [20, 28, 440, "500 x 28A ou 500A Standard"],
                [20, 32, 440, "500A ou 500 x 32A"],
                [20, 37, 440, "500 x 35A ou 500A Confort/Ballon"],
                [20, 40, 440, "500 x 38A"],
                [22, 47, 457, ""],
                [22, 44, 484, ""],
                [22, 25, 489, ""],
                [22, 32, 489, "550 x 32 ANL"],
                [22, 40, 489, ""],
                [22, 50, 489, ""],
                [22, 28, 490, "550 x 28A ou 550A Standard"],
                [22, 32, 490, "550 x 32A ou 550A"],
                [22, 37, 490, "550 x 35A ou 550A Confort/Ballon"],
                [22, 37, 498, ""],
                [22, 28, 501, ""],
                [22, 32, 501, ""],
                [22, 37, 501, ""],
                [24, 19, 507, ""],
                [24, 25, 507, ""],
                [24, 37, 507, ""],
                [24, 40, 507, ""],
                [24, 47, 507, ""],
                [24, 49, 507, ""],
                [24, 50, 507, ""],
                [24, 51, 507, ""],
                [24, 54, 507, ""],
                [24, 57, 507, ""],
                [24, 60, 507, ""],
                [24, 62, 507, ""],
                [24, 65, 507, ""],
                [24, 70, 507, ""],
                [24, 75, 507, ""],
                [24, 100, 507, ""],
                [24, 18, 520, ""],
                [24, 20, 520, ""],
                [24, 22, 520, ""],
                [24, 23, 520, ""],
                [24, 25, 520, ""],
                [24, 28, 520, ""],
                [24, 47, 520, ""],
                [25, 57, 520, ""],
                [24, 44, 531, ""],
                [24, 40, 534, "600 x 38B"],
                [24, 45, 534, "600 x 45B"],
                [24, 20, 540, ""],
                [24, 25, 540, ""],
                [24, 28, 540, "600 x 28A"],
                [24, 32, 540, ""],
                [24, 37, 540, "600 x 35A ou 600A Confort"],
                [24, 40, 540, "600 x 38A"],
                [24, 22, 541, "600 x 22A"],
                [24, 25, 541, "600 x 25A"],
                [24, 28, 541, "600 x 28A ou 600A Standard"],
                [24, 32, 541, "600 x 32A ou 600A"],
                [24, 37, 541, "600 x 35A ou 600A Confort/Ballon"],
                [24, 32, 547, ""],
                [26, 20, 559, ""],
                [26, 25, 559, ""],
                [26, 28, 559, ""],
                [26, 32, 559, ""],
                [26, 35, 559, ""],
                [26, 37, 559, ""],
                [26, 40, 559, ""],
                [26, 42, 559, ""],
                [26, 44, 559, ""],
                [26, 47, 559, "650 x 45 ou 650 x 47"],
                [26, 50, 559, ""],
                [26, 51, 559, ""],
                [26, 54, 559, "650 x 50"],
                [26, 56, 559, ""],
                [26, 57, 559, ""],
                [26, 60, 559, ""],
                [26, 62, 559, ""],
                [26, 65, 559, ""],
                [26, 70, 559, ""],
                [26, 75, 559, ""],
                [26, 19, 571, ""],
                [26, 20, 571, "650 x 20C"],
                [26, 22, 571, ""],
                [26, 23, 571, "650 x 22C ou 650 x 23C"],
                [26, 25, 571, ""],
                [26, 40, 571, "650 x 35C ou 650 x 38C ou 650 x 40C"],
                [26, 47, 571, "650 x 45C ou 650CS Confort ou 650 x 45C ou 650 CSC"],
                [26, 54, 571, "650 x 50C"],
                [26, 28, 584, "650 x 28B"],
                [26, 32, 584, "650 x 32B"],
                [26, 35, 584, "650 x 35B ou 650B Standard"],
                [26, 37, 584, "650 x 35B"],
                [26, 40, 584, "650 x 35B ou 650B Standard ou 650 x 38B ou 650B Semi-Confort ou 650 x 42B"],
                [26, 44, 584, "650 x 42B ou 650B Semi-Confort"],
                [26, 45, 584, "650 x 45B"],
                [26, 54, 584, ""],
                [27.5, 30, 584, ""],
                [27.5, 50, 584, ""],
                [27.5, 70, 584, ""],
                [26, 20, 590, "650 x 20A"],
                [26, 25, 590, "650 x 25A"],
                [26, 28, 590, "650 x 28A"],
                [26, 32, 590, "650 x 32A"],
                [26, 35, 590, "650 x 35A ou 650A"],
                [26, 37, 590, "650 x 35A ou 650A"],
                [26, 40, 590, "650 x 38A"],
                [26, 44, 590, "650 x 40A"],
                [26, 32, 597, ""],
                [27, 37, 609, ""],
                [27, 40, 609, ""],
                [28, 54, 609, ""],
                [27, 20, 630, ""],
                [27, 22, 630, ""],
                [27, 25, 630, ""],
                [27, 28, 630, ""],
                [27, 32, 630, ""],
                [27, 35, 630, ""],
                [28, 18, 622, "700 x 18C"],
                [28, 19, 622, "700 x 19C"],
                [28, 20, 622, "700 x 20C"],
                [28, 21, 622, "700 x 21C"],
                [28, 22, 622, "700 x 22C"],
                [28, 23, 622, "700 x 23C"],
                [28, 25, 622, "700 x 25C"],
                [28, 28, 622, "700 x 28C ou 700 x 30C ou 700C Carrera"],
                [28, 30, 622, "700 x 28C ou 700 x 30C"],
                [28, 32, 622, "700 x 32C ou 700C Course"],
                [28, 34, 622, "700 x 34C"],
                [28, 35, 622, "700 x 35C"],
                [28, 37, 622, "700 x 35C ou 700 x 37C"],
                [28, 38, 622, "700 x 38C"],
                [28, 40, 622, "700 x 38C ou 700 x 40C"],
                [28, 42, 622, "700 x 40C ou 700 x 42C"],
                [28, 44, 622, "700 x 42C"],
                [28, 47, 622, "700 x 42C ou 700 x 45C ou 700 x 47C"],
                [28, 50, 622, "700 x 48C ou 700 x 50C"],
                [28, 54, 622, ""],
                [28, 57, 622, ""],
                [28, 60, 622, ""],
                [28, 62, 622, ""],
                [28, 28, 635, "700B"],
                [28, 32, 635, "700 x 28B ou 700B Course ou 700B"],
                [28, 40, 635, "700 x 38B ou 700 x 35B ou 700B Standard ou 700 Standard"],
                [28, 44, 635, "700 x 40/42B"],
                [28, 28, 642, "700 x 28A"],
                [28, 37, 642, "700 x 35A"],
                [30, 37, 700, ""]
                ]
                



                                                                                                                                                                                                                                                                                                                                                                                 








import numpy as np
print("CALCULATEUR ETRTO POUR MESURER LES CHAMBRES À AIR")
print("Ce court programme permet de déterminer les normes ETRTO (et françaises si possible) d'une chambre à air inidentifiée, c'est à dire qui n'a pas de marquage. Cela se fait à partir de deux mesure simples.")
print("Avant d'entrer ces mesures, le programme propose un facteur de correction visant à rattrapper les potentielles erreurs de mesures. Si vous n'avez pas l'habitude du logiciel, appuyez sur Entrée à cette étape.")
print("Les mesures se prennent avec la chambre à air dégonflée:")
print("   - d'abord, mesurer la longueur (en mm) de la chambre à air mise à plat sans l'étirer")
print("   - enfin, mesurer la largeur (en mm) de la chambre à air applatie")
print("Entrez ces mesures l'une après l'autre, et le logiciel vous fournira la norme la plus proche !")




facteur = input("Facteur de correction (appuyer sur entrer pour avoir le facteur par défaut de 1.1):")
if facteur == "":
    facteur = 1.1
else:
    facteur = float(facteur)

longueur = float(input("Longueur de la CAA (mm):"))
largeur = float(input("Largeur de la CAA (mm):"))
pi = 3.14159
long_diam = facteur*2*longueur/pi
larg_diam = facteur*2*largeur/pi
print("ETRTO de la mesure:  "+str(int(long_diam))+" - "+str(int(larg_diam)))
mindifdiam = 100000000000
indmindifdiam = 0
for i in range(len(table_normes)):
    diam = table_normes[i][2]
    ecart = abs(diam - long_diam)
    if ecart<mindifdiam:
        mindifdiam = ecart
        indmindifdiam = i
diam_norme = table_normes[indmindifdiam][2]
bondiam = []
for i in range(len(table_normes)):
    if table_normes[i][2] == diam_norme:
        bondiam.append(table_normes[i])

mindiflarg = 100000000000
indmindiflarg = 0
for i in range(len(bondiam)):
    diam = bondiam[i][1]
    ecart = abs(diam - larg_diam)
    if ecart< mindiflarg:
        mindiflarg = ecart
        indmindiflarg = i

ETRTO_norme = bondiam[indmindiflarg]

print("La meilleure correspondance ETRTO à votre mesure:  " + str(ETRTO_norme[2]) + " - "+str(ETRTO_norme[1]))
print("C'est donc pour une roue de "+str(ETRTO_norme[0])+" pouces")
if ETRTO_norme[3] != "":
    print("La norme française correspondante est la suivante: "+ ETRTO_norme[3])
else:
    print("À cette norme ETRTO ne correspond pas de norme française.")
print("\n")
print("Pour plus d'informations, visitez le Wiklou ! https://wiklou.org/wiki/ETRTO_(ISO_5775)")
print("Programme créé par Lou Bedouret à partir des données du Wiklou")
input("Merci d'avoir utilisé ce programme ! Pressez Entrée pour terminer :)")