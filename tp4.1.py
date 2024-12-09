class StringFoo:
   def __init__(self):
       self.message = "fortnite"


   def set_string(self, new_string):
       self.message = new_string


   def print_string(self):
       print(self.message)

class Rectangle:
   def __init__(self, largeur, longueur):
       self.largeur = largeur
       self.longueur = longueur


   def calcul_aire(self):
       return self.largeur * self.longueur


   def afficher_infos(self):
       print(f"largeur: {self.largeur}, longeur: {self.longueur}, aire: {self.calcul_aire()}")



from math import pi


class Cercle:
   def __init__(self, r):
       self.r = r


   def calcul_aire(self):
       return self.r * self.r * pi


   def calcul_circonference(self):
       return self.r * 2 * pi


   def afficher_infos(self):
       print(f"rayon: {self.r}, aire: {self.calcul_aire()}, circonférence: {self.calcul_circonference()}")

from random import randint


class Hero:
   def __init__(self, nom):
       self.points_vie = randint(1, 6) + randint(1, 6)
       self.force_attaque = randint(1, 6)
       self.force_defense = randint(1, 6)
       self.nom = nom
   def faire_attaque(self):
       return self.force_attaque + randint(1, 6)
   def recevoir_dommages(self, qte_dommages):
       self.points_vie -= qte_dommages - self.force_defense
   def est_vivant(self):
       return self.points_vie > 0






from random import randint
from dataclasses import dataclass


@dataclass
class CaracteristiquesPersonnage:
   force: int = randint(1, 20),
   dexterite: int = randint(1, 20),
   constitution: int = randint(1, 20),
   intelligence: int = randint(1, 20),
   sagesse: int = randint(1, 20),
   charisme: int = randint(1, 20)


class Hero:
  def __init__(self, nom):
      self.points_vie = randint(1, 6) + randint(1, 6)
      self.force_attaque = randint(1, 6)
      self.force_defense = randint(1, 6)
      self.nom = nom
      self.stats = CaracteristiquesPersonnage()
  def faire_attaque(self):
      return self.force_attaque + randint(1, 6)
  def recevoir_dommages(self, qte_dommages):
      self.points_vie -= qte_dommages - self.force_defense
  def est_vivant(self):
      return self.points_vie > 0
