'''
Created on 26 mai 2015

@author: fcarluer
'''
import os
from random import randrange
from math import ceil
from Crypto.Random.random import randrange

#Déclaration des variables de départ
money = 1000
continuerPartie = True


print("Vous voilà installé avec", money," $.")

while continuerPartie:
    choix = -1
    while choix <0 or choix > 49:
        choix = input("quel chiffre voulez-vous (entre 0 et 49)")
        try:
            choix = int(choix)
        except ValueError:
            print("Vous n'avez pas choisi")
            choix = -1
            continue
        if choix < 0:
            print("blaireau neg")
        if choix > 49:
            print("blaireau pos")
    
    mise = 0
    while mise <= 0 or mise > money:
        mise = input("combien tu mises?")
        try:
            mise = int(mise)
        except ValueError:
            print("vous n'avez pas miser de fric")
            mise = -1
            continue
        if mise <= 0:
            print("mise negative ou nulle gringo")
        if mise > money:
            print("t'as pas assez de cash,  Gringo!!!! il ne te reste que ", money, "$")
    
    numero=randrange(50)
    print("La roulette tourne.... et s'arrete sur : ", numero)
            
    if numero == choix:
        gain = mise*3-mise
        money += gain
        print("Bravo Gringo tu as gagné : ",gain)
    elif numero%2 == mise%2:
        gain = ceil(mise*0.5)-mise
        money += gain
        print("bonne couleur Gringo tu as gagné : ",gain)
    else:
        money -= mise
        print("hin hin hin t'as perdu il te reste :")    
        
    # On interrompt la partie si le joueur est ruiné
    if money <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False
    else:
        # On affiche l'argent du joueur
        print("Vous avez à présent", money, "$")
        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False

# On met en pause le système (Windows)
os.system("pause")

if __name__ == '__main__':
    numero = randrange(50)
    print("numero aléatoire généré : ",numero)
    pass