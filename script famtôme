# coding: utf-8


import csv
import requests
from bs4 import BeautifulSoup
#après m'être créer un environement virtuel, j'importe le module Beautiful soupe qui va m'aider a faire la moisson sur mon site internet choisi.

url1 = "http://www.csc-scc.gc.ca/divulgation-contrats/2015-2016/2015-2016_4-fra.shtml"
# j'ai choisi le site du ministère du sytème correctionnel du canada, l'onglet : Contrats de 2015-2016 - Quatrième trimestre.

fichier = "correctionnel.csv"
#j'ai créer un document csv dans lequel tout le contenu de mon site s'y retrouve. c'est dans ce document que j'effectue ma moisson.

entetes = {
	"User-Agent":"Frédérique De Simone - Requête envoyée dans le cadre d'un cours d'informatique à l'UQAM",
	"From":"frederique.desimone@gmail.com"
}
contenu = requests.get(url1, headers=entetes)
page = BeautifulSoup(contenu.text,"html.parser")
#print(page)

i = 0
# cette fonction est le compteur qui va ramasser l'information dans le tableau de ma page choisie.
#chaque ligne du tableau est en tr et chaque colonne est en td

for ligne in page.find_all("tr"):
    # cette fonction permet de rammasser toute les valeurs en tr 
   
    if i > 0:
# i étant la premiere ligne est inutile, donc on l'enlève.
#i > 0 = i != 0
        #print(ligne)
        lien = ligne.a.get("href")
        #print(lien)
        lien = "http://www.csc-scc.gc.ca/divulgation-contrats/2015-2016/" + lien
        #print(lien)
#la rectte de base de soupe est faite. Maintenant, je peux commencer à explorer.

        contenu2 = requests.get(lien,headers=entetes)
        page2 = BeautifulSoup(contenu2.text,"html.parser")
# je créer une liste dans laquelle s'y trouvera les contrats et se qui s'y rapporte.     
        contrat = []
    
        contrat.append(lien)

#j'ajoute le lien pour chacun des contrats pour effectuer des vérifications.  
# je fais une boucle qui va aller chercher tous les éléments du tableau.

        for item in page2.find_all("tr"):
            #print(item)
#pour éviter que des cellules vides ne fassent planter le système, on écrit la variable :        
            if item.td is not None:
                contrat.append(item.td.text)
                
            else:
                contrat.append(None)
#j'ajoute none (nean) à la liste                
        print(contrat)

#comme avec l'api, je fais un nouveau dossier et ca inscrit la liste de contrats dans une nouvelle liste csv.        
        chose = open(fichier,"a")
        correction = csv.writer(chose)
        correction.writerow(contrat)
        
#ensuite, j'augmente le compteur de 1        
    i += 1

for ligne in lien:
 	i += 1
 	print("On a {} services".format(i))
print(i)

f1 = open(fichier)
lignes = f1.readlines()
for ligne in f1:
    print(ligne.rfind("/"))

# je ne comprends pas tout ce qui est imprimé sur mon terminal. En fait, oui je comprends, mais je me sens perdue.
#je ne sais pas trop quoi faire avec toute l'information. j'ai du mal à démeler l'info. 

#il me semble plus clair et plus simple de lire le tableau sur le site internet du ministère des services correctionnels du canada.
#j'aimerais pouvoir farfouiller dans tous le matériel que j'ai ammassé, mais je ne sais pas ce que je cherche.

# j'ai essayé beaucoup de formules, mais soit rien ne se produit, soit j'ai des erreurs de syntaxe ou soit ma recherche n'est pas permise.
# j'aurais aimé avoir un lexique avec des listes de vocabulaire, de formules ou des exemples de boucles pour chercher précisément dans mes données, une fois la soupe complétée. 

#je pense qu'il m'aurait peut-être fallu un cours de moissonnage supplémentaire, avant de pouvoir faire le travail de moisson par moi-même.

# je sais qu'a l'étape où j'en suis, il ne me reste qu'à créer des boucles plus spécifiques à ma racherche. Mais je ne connais pas le voccabulaire adéquat.
# je comprends le principe de la boucle et de la méchanique de python, mais vraiment réussir à l'appliquer, me dépasse un peu. 

#je sais qu'avec un  cours de plus sur la moisson j'aurais été en mesure de faire des recherches plus exhaustives.
#je crois que je suis en mesure d'utiliser python et la moisson, mais qu'il me manque simplement d'outils.

#ma recommandation pour un prochain travail, ou pour la prochaine fois que le cours sera donné :
# passer plus de temps à expliquer la moisson;
#fournir aux étudiants un lexique ou une base de données avec des exemples de vocabulaire ou de formules;
#et donner aux étudiants plus d'exercices à faire par eux-mêmes, en classe. 

# je crois que vous expliquer bien la matière, mais nous avons surtout appris à faire comme vous et non, à nous débrouiller par nous-même.
    
