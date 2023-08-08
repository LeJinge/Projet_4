from Model.joueur import Joueur
from Controller.gestion_joueur import Creation_de_joueur
from Controller.gestion_joueur import GestionJoueurs

import json

gestion_joueurs = GestionJoueurs()
creation_joueur = Creation_de_joueur(gestion_joueurs)

# Appeler la méthode de création de joueur manuellement
nouveau_joueur = creation_joueur.creer_joueur_manuellement()

# Ajouter le nouveau joueur à la liste gérée par GestionJoueurs
gestion_joueurs.ajouter_joueur(nouveau_joueur)

# Sauvegarder les données dans le fichier JSON
gestion_joueurs.sauvegarder_donnees()