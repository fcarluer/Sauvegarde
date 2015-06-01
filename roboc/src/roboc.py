# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte
RepertoireCarte="../cartes"
# On charge les cartes existantes

cartes = []
for nom_fichier in os.listdir(RepertoireCarte):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join(RepertoireCarte, nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte, à compléter
            print("création du labyrinth {}.".format(nom_carte))
            cartes.append(Carte(nom_carte,contenu)) 
    elif nom_fichier.endswith(".sav"):
        print("0 - Sauvegarde")
# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
