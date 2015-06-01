# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
from labyrinthe import Labyrinthe
from donnees import *


class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = self.creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)
    
    def CalculerCoordonees(self, position, largeur):
        #Determine les coordonées X et Y en fonction de la position du caractere
        position = position
        taille = largeur+1
        posX = position%taille
        posY = int(position/taille)
        return ("x{}-y{}".format(posX, posY))
    
    
    def creer_labyrinthe_depuis_chaine(self, chaine):
        #On extrait les coordonées du Robot et les differents obstacles
        self.chaine = chaine

        #Définition des Elements de la carte

        largeur = chaine.find("\n")
        obstacles ={}
        positionRobot=chaine.find(roboc)
        robot=self.CalculerCoordonees(positionRobot,largeur)
        index=0
        for caractere in chaine:
            if caractere == murs:
                pos = self.CalculerCoordonees(index,largeur)
                #print("position:{} de type : {}".format(pos,"murs"))
                obstacles[pos]=murs
            elif caractere == roboc:
                pos = self.CalculerCoordonees(index,largeur)
                #print("position:{} de type : {}".format(pos,"roboc"))    
                obstacles[pos]=roboc
            elif caractere == vide:
                pos = self.CalculerCoordonees(index,largeur)
                #print("position:{} de type : {}".format(pos,"roboc"))    
                obstacles[pos]=vide
            elif caractere == porte:
                pos = self.CalculerCoordonees(index,largeur)
                #print("position:{} de type : {}".format(pos,"porte"))    
                obstacles[pos]=porte                
            elif caractere == sortie:
                pos = self.CalculerCoordonees(index,largeur)
                print("position:{} de type : {}".format(pos,"sortie"))
                obstacles[pos]=sortie
            elif caractere == Escalier:
                pos = self.CalculerCoordonees(index,largeur)
                #print("position:{} de type : {}".format(pos,"Escalier"))     
                obstacles[pos]=Escalier                 
            elif caractere == retour:
                pos = self.CalculerCoordonees(index,largeur)
                #print("position:{} de type : {}".format(pos,"retour"))
                obstacles[pos]=retour
            index +=1
        
            
        lab = Labyrinthe(robot, obstacles)
        print("on avance de 1")
        if lab.isObstacle("x0-y1"):
            print("youpi")
        else:
            print("ouin")

        

   

