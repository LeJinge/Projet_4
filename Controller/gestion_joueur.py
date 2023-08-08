from Model.joueur import Joueur

import json


class Creation_de_joueur:
    def __init__(self, gestion_joueurs):
        self.gestion_joueurs = gestion_joueurs

    def creer_joueur_manuellement(self):
        prenom = input("Entrez le prénom du joueur : ")
        nom =  input("Entrez le nom du joueur : ")
        date_de_naissance = input("Entrez la date de naissance du joueur : ")

        nouveau_joueur = Joueur(nom, prenom, date_de_naissance)
        self.gestion_joueurs.ajouter_joueur(nouveau_joueur)

        return nouveau_joueur

class GestionJoueurs:
    def __init__(self):
        self.donnees = self.charger_donnees()

    def charger_donnees(self):
        try:
            with open("donnees.json", "r", encoding="utf-8") as fichier:
                return json.load(fichier)
        except FileNotFoundError:
            return {"joueurs": []}

    def joueur_existe(self, nouveau_joueur):
        for joueur in self.donnees["joueurs"]:
            if joueur["nom"] == nouveau_joueur.nom and joueur["prenom"] == nouveau_joueur.prenom:
                return True
        return False

    def ajouter_joueur(self, nouveau_joueur):
        if not self.joueur_existe(nouveau_joueur):
            nouveau_joueur_dict = vars(nouveau_joueur)
            self.donnees["joueurs"].append(nouveau_joueur_dict)

    def sauvegarder_donnees(self):
        with open("donnees.json", "w", encoding="utf-8") as fichier:
            json.dump(self.donnees, fichier, indent=4, ensure_ascii=False)