from Model.tournoi import Tournoi
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

            if not self.gestion_joueur.joueur_existe(nom_joueur, prenom_joueur):  # Utilisez la méthode de gestion_joueur.py

                print(f"Le joueur {prenom_joueur} {nom_joueur} n'existe pas. Veuillez le créer.")
                date_naissance_joueur = input("Date de naissance du joueur (format DD/MM/YYYY) : ")
                self.gestion_joueur.ajouter_joueur(nom_joueur, prenom_joueur, date_naissance_joueur)

            # Supposant que Joueur est une classe que vous avez définie ailleurs, et que la méthode ajouter_joueur renvoie un objet Joueur
            joueur_obj = self.gestion_joueur.recuperer_joueur(nom_joueur, prenom_joueur)
            nouveau_tournoi.liste_joueurs_enregistres.append(joueur_obj)

        print(f"Joueurs ajoutés au tournoi {nouveau_tournoi.nom}.")

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
                self.tournois = [self.dict_vers_tournoi(data) for data in liste_tournois_dict]
        except FileNotFoundError:
            pass

    def tournoi_vers_dict(self, tournoi):
        data = {
            "nom": tournoi.nom,
            "lieu": tournoi.lieu,
            "date_debut": tournoi.date_debut,
            "date_fin": tournoi.date_fin,
            "nombre_tours": tournoi.nombre_tours,
            "tour_actuel": tournoi.tour_actuel,
            "liste_tours": tournoi.liste_tours,
            # Assurez-vous que les éléments de cette liste sont sérialisables en JSON
            "liste_joueurs_enregistres": [joueur_vers_dict(joueur) for joueur in tournoi.liste_joueurs_enregistres],
            # Supposant que vous ayez une fonction joueur_vers_dict pour transformer un joueur en dict
            "description": tournoi.description
        }
        return data

    def dict_vers_tournoi(self, data):
        return Tournoi(data["nom"], ...)

    def set_vue(self, vue):
        self.vue_tournoi = vue

    def ajouter_joueurs_depuis_json(self):
        # Étape 1 : Chargement de la liste des joueurs
        joueurs = []
        try:
            with open("joueurs.json", "r", encoding="utf-8") as fichier:
                data = json.load(fichier)
                joueurs = data["joueurs"]
        except FileNotFoundError:
            print("Fichier joueur.json non trouvé.")
            return

        # Étape 2 : Affichage et sélection des joueurs
        joueurs_selectionnes = []
        print("Veuillez sélectionner les joueurs pour le tournoi (entrez le numéro du joueur) :")
        for index, joueur in enumerate(joueurs, 1):
            print(f"{index}. {joueur['nom']} {joueur['prenom']}")

        while True:
            try:
                choix = int(input("Sélectionnez un joueur (ou 0 pour terminer) : "))
                if choix == 0:
                    break
                joueur_selectionne = joueurs[choix - 1]
                joueurs_selectionnes.append(joueur_selectionne)
            except (ValueError, IndexError):
                print("Choix invalide. Veuillez réessayer.")

        # Étape 3 : Ajout des joueurs au tournoi
        if not self.tournoi:
            print("Aucun tournoi actif. Veuillez d'abord créer un tournoi.")
            return

        dernier_tournoi = self.tournoi[-1]  # On prend le dernier tournoi ajouté
        for joueur_dict in joueurs_selectionnes:
            joueur_obj = Joueur(joueur_dict["nom"], joueur_dict["prenom"], joueur_dict["date_de_naissance"])
            dernier_tournoi.liste_joueurs_enregistres.append(joueur_obj)

        print(f"{len(joueurs_selectionnes)} joueurs ont été ajoutés au tournoi.")