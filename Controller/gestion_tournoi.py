from Model.tournoi import Tournoi
from Model.joueur import Joueur
from Vue.affichage_tournoi import AffichageTournoi
from Controller.gestion_joueur import GestionJoueurs
from tinydb import TinyDB, Query

class GestionTournoi:
    def __init__(self):
        self.vue_tournoi = AffichageTournoi()
        self.tournoi = []
        self.db = TinyDB('tournois.json')
        self.gestion_joueur = GestionJoueurs()
        self.charger_donnees()

    def creer_tournoi(self, nom, lieu, date_debut, date_fin, nombre_tours, description):
        # Suppression du tournoi existant avec le même nom
        self.tournoi = [tournoi for tournoi in self.tournoi if tournoi.nom != nom]

        # Initialisation d'un nouveau tournoi
        nouveau_tournoi = Tournoi(nom, lieu, date_debut, date_fin, nombre_tours, description)
        self.tournoi.append(nouveau_tournoi)

        print("\nVeuillez entrer les joueurs pour le tournoi :")
        for _ in range(nombre_tours * 2):
            identifiant_echec = input("\nIdentifiant National d'échec du joueur (ou 'stop' pour arrêter): ")
            if identifiant_echec.lower() == 'stop':
                break

            joueur_temp = self.gestion_joueur.recuperer_joueur(identifiant_echec=identifiant_echec)

            nom_joueur = input("Nom du joueur (ou 'stop' pour arrêter): ")
            if nom_joueur.lower() == 'stop':
                break

            prenom_joueur = input("Prénom du joueur (ou 'stop' pour arrêter): ")
            if prenom_joueur.lower() == 'stop':
                break

            if not joueur_temp:
                print(f"Le joueur avec l'Identifiant National d'échec {identifiant_echec} n'existe pas.")
                date_naissance_joueur = input(
                    "Date de naissance du joueur (format DD/MM/YYYY ou 'stop' pour arrêter) : ")
                if date_naissance_joueur.lower() == 'stop':
                    break
                joueur_temp = Joueur(nom_joueur, prenom_joueur, date_naissance_joueur, identifiant_echec)
                self.gestion_joueur.ajouter_joueur(joueur_temp)
            else:
                if joueur_temp.nom != nom_joueur or joueur_temp.prenom != prenom_joueur:
                    print("Erreur: Le nom et prénom fournis ne correspondent pas à l'identifiant national d'échec.")
                    continue

            nouveau_tournoi.liste_joueurs_enregistres.append(joueur_temp)
            self.sauvegarder_donnees()  # Sauvegarde

    def afficher_infos_tournoi(self):
        for tournoi in self.tournoi:
            self.vue_tournoi.afficher_infos_tournoi(tournoi)

    def sauvegarder_donnees(self):
        liste_tournois_dict = [self.tournoi_vers_dict(tournoi) for tournoi in self.tournoi]
        self.db.insert_multiple(liste_tournois_dict)

    def charger_donnees(self):
        liste_tournois_dict = self.db.all()
        self.tournoi = [self.dict_vers_tournoi(data) for data in liste_tournois_dict]

    def set_vue(self, vue):
        self.vue_tournoi = vue

    @staticmethod
    def joueur_vers_dict(joueur):
        return {
            "nom": joueur.nom,
            "prenom": joueur.prenom,
            "date_de_naissance": joueur.date_de_naissance,
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
            "liste_joueurs_enregistres": [GestionTournoi.joueur_vers_dict(joueur) for joueur in tournoi.liste_joueurs_enregistres],
            "description": tournoi.description
        }
        return data

    def dict_vers_tournoi(self, data):
        tournoi = Tournoi(
            data["nom"],
            data["lieu"],
            data["date_debut"],
            data["date_fin"],
            data["nombre_tours"],
            data["description"]
        )
        tournoi.tour_actuel = data["tour_actuel"]
        tournoi.liste_tours = data["liste_tours"]

        # Convertir les dictionnaires joueur en instances de Joueur
        for joueur_dict in data["liste_joueurs_enregistres"]:
            joueur = Joueur(joueur_dict["nom"], joueur_dict["prenom"], joueur_dict["date_de_naissance"])
            tournoi.liste_joueurs_enregistres.append(joueur)

        return tournoi

    def charger_tournoi(self, nom):
        self.charger_donnees()  # Charger toutes les données du fichier

        # Recherchez le tournoi par son nom
        for tournoi in self.tournoi:
            if tournoi.nom == nom:
                return tournoi
        print("Tournoi non trouvé.")
        return None