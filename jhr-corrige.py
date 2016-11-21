# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

url1 = "http://www.csc-scc.gc.ca/divulgation-contrats/2015-2016/2015-2016_4-fra.shtml"

fichier = "correctionnel-JHR.csv"

entetes = {
	"User-Agent":"Frédérique De Simone - Requête envoyée dans le cadre d'un cours d'informatique à l'UQAM",
	"From":"frederique.desimone@gmail.com"
}

contenu = requests.get(url1, headers=entetes)
page = BeautifulSoup(contenu.text,"html.parser")
#print(page)

i = 0

for ligne in page.find_all("tr"):
   
    if i > 0:
        #print(ligne)
        lien = ligne.a.get("href")
        #print(lien)
        lien = "http://www.csc-scc.gc.ca/divulgation-contrats/2015-2016/" + lien

        contenu2 = requests.get(lien,headers=entetes)
        page2 = BeautifulSoup(contenu2.text,"html.parser")

        contrat = []
        contrat.append(lien)

        for item in page2.find_all("tr"):
            #print(item)
            if item.td is not None:
                contrat.append(item.td.text)
            else:
                contrat.append(None)

        print(contrat)

        chose = open(fichier,"a")
        correction = csv.writer(chose)
        correction.writerow(contrat)
        
    i += 1

# Ça fonctionne bien, bravo! Le CSV produit contient toutes les informations recherchées. Tu as appliqué la recette de moissonnage à un autre site web.
# Je te remercie pour tes recommandations. Elles font beaucoup de sens. Je vais les appliquer dans les prochaines itérations de ce cours :)

# Les lignes ci-dessous subsistaient dans ton script. Elles ne modifiaient pas la production du CSV, mais sont inutiles.

# for ligne in lien:
#  	i += 1
#  	print("On a {} services".format(i))
# print(i)

# f1 = open(fichier)
# lignes = f1.readlines()
# for ligne in f1:
#     print(ligne.rfind("/"))
