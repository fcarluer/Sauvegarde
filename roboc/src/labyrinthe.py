# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""
from donnees import *

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = obstacles
        
    def isObstacle(self,robot):
        if self.grille[robot]==murs:
            return(False)
        #if robot in self.grille()==murs:
        #    print("caca")
        # ...