from Model.tournoi import Tournoi
from Model.joueur import Joueur
from Vue.affichage_tournoi import AffichageTournoi
from Controller.gestion_joueur import GestionJoueurs  # Import de la classe GestionJoueur
import json


class GestionTournoi:
    def __init__(self):
        self.vue_tournoi = AffichageTournoi()
        self.tournoi = []
        self.gestion_joueur = GestionJoueurs()  # Instance de GestionJoueur

    def creer_tournoi(self, nom, lieu, date_debut, date_fin, nombre_tours=4, description=""):
        nouveau_tournoi = Tournoi(nom, lieu, date_debut, date_fin, nombre_tours, description)
        self.tournoi.append(nouveau_tournoi)

        print("Veuillez entrer les joueurs pour le tournoi :")
        for _ in range(nombre_tours * 2):
            nom_joueur = input("Nom du joueur: ")
            prenom_joueur = input("Prénom du joueur: ")

            # Vérifiez d'abord si le joueur existe
            joueur_temp = self.gestion_joueur.recuperer_joueur(nom_joueur, prenom_joueur)

            if not joueur_temp:
                # Si le joueur n'existe pas, recueillez les informations nécessaires et créez le joueur
                print(f"Le joueur {prenom_joueur} {nom_joueur} n'existe pas.")
                date_naissance_joueur = input("Date de naissance du joueur (format DD/MM/YYYY) : ")
                joueur_temp = Joueur(nom_joueur, prenom_joueur, date_naissance_joueur)
                self.gestion_joueur.ajouter_joueur(joueur_temp)
            else:
                # Ici, le joueur existe déjà dans le système
                pass

            # Ajoutez le joueur à la liste des joueurs enregistrés pour le tournoi
            nouveau_tournoi.liste_joueurs_enregistres.append(joueur_temp)

        print(f"Joueurs ajoutés au tournoi {nouveau_tournoi.nom}.")
        self.sauvegarder_donnees()

    def afficher_infos_tournoi(self):
        if self.tournoi:
            self.vue_tournoi.afficher_infos_tournoi(self.tournoi)
        else:
            print("Aucun tournoi n'est créé.")

    def sauvegarder_donnees(self):
        with open("tournoi.json", "w", encoding="utf-8") as fichier:
            liste_tournois_dict = [self.tournoi_vers_dict(tournoi) for tournoi in self.tournoi]
            json.dump(liste_tournois_dict, fichier, ensure_ascii=False, indent=4)

    def charger_donnees(self):
        try:
            with open("tournoi.json", "r", encoding="utf-8") as fichier:
                liste_tournois_dict = json.load(fichier)
                self.tournoi = [self.dict_vers_tournoi(data) for data in liste_tournois_dict]
        except FileNotFoundError:
            pass

    def set_vue(self, vue):
        self.vue_tournoi = vue

    def joueur_vers_dict(joueur):
        if isinstance(joueur, dict):
            return joueur
        return {
            "nom": joueur.nom,
            "prenom": joueur.prenom,
            "date_de_naissance": joueur.date_de_naissance,
            "classement": joueur.classement
        }

    def tournoi_vers_dict(self, tournoi):
        data = {
            "nom": tournoi.nom,
            "lieu": tournoi.lieu,
            "date_debut": tournoi.date_debut,
            "date_fin": tournoi.date_fin,
            "nombre_tours": tournoi.nombre_tours,
            "tour_actuel": tournoi.tour_actuel,
            "liste_tours": tournoi.liste_tours,
            "liste_joueurs_enregistres": [GestionTournoi.joueur_vers_dict(joueur) for joueur in
                                          tournoi.liste_joueurs_enregistres],
            "description": tournoi.description
        }
        return data
