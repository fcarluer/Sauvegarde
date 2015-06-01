'''
Created on 28 mai 2015

@author: fcarluer

'''
class Personne: # Définition de notre classe Personne
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    
    def __init__(self, nom, prenom): # Notre méthode constructeur
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self.nom = nom
        self.prenom = prenom # Quelle originalité
        self.age = 33 # Cela n'engage à rien
        self._lieu_residence = "Paris"
    def _get_lieu_residence(self):
        print("Acces à la méthode de lecture de résidence")
        return self._lieu_residence
    def _set_lieu_residence(self,nouvelle_adresse):
        print("Changement d'adresse, {} déménage à {}.".format(self.prenom, nouvelle_adresse))
        self._lieu_residence = nouvelle_adresse
    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "Personne: nom({}), prénom({}), âge({}), ville({})".format(
                self.nom, self.prenom, self.age, self.lieu_residence)
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)

class Compteur:
    objets_crees = 0
    def __init__(self):
        Compteur.objets_crees += 1
    def combien(cls):
        print("jusqu'a present, {} objets ont été créés. ".format(cls.objets_crees))
    combien = classmethod(combien)
class TableauNoir:
    def __init__(self):
        self.surface = ""
    def ecrire(self,message_a_ecrire):
        if self.surface !="":
            self.surface += "\n"
        self.surface += message_a_ecrire