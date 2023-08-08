import json
from Model.joueur import Joueur

class GestionJoueurs:
    def __init__(self):
        self.donnees = self.charger_donnees()

    def charger_donnees(self):
        try:
            with open("joueurs.json", "r", encoding="utf-8") as fichier:
                return json.load(fichier)
        except FileNotFoundError:
            return {"joueurs": []}

    def joueur_existe(self, nouveau_joueur):
        for joueur in self.donnees["joueurs"]:
            if joueur["nom"] == nouveau_joueur.nom and joueur["prenom"] == nouveau_joueur.prenom:
                return True
        return False

    def ajouter_joueur(self, nouveau_joueur):
        if self.joueur_existe(nouveau_joueur):
            self.vue_joueur.afficher_message("Ce joueur existe déjà dans la liste, doublon non ajouté.")
        else:
            self.donnees["joueurs"].append(vars(nouveau_joueur))
            self.sauvegarder_donnees()

    def sauvegarder_donnees(self):
        with open("joueurs.json", "w", encoding="utf-8") as fichier:
            json.dump(self.donnees, fichier, indent=4, ensure_ascii=False)

    def set_vue(self, vue_joueur):
        self.vue_joueur = vue_joueur

class CreationDeJoueur:
    def __init__(self, gestion_joueurs):
        self.gestion_joueurs = gestion_joueurs

    def creer_joueur_manuellement(self):
        prenom = self.gestion_joueurs.vue_joueur.demander_information("Entrez le prénom du joueur : ")
        nom = self.gestion_joueurs.vue_joueur.demander_information("Entrez le nom du joueur : ")
        date_de_naissance = self.gestion_joueurs.vue_joueur.demander_information("Entrez la date de naissance du joueur : ")

        nouveau_joueur = Joueur(nom, prenom, date_de_naissance)
        self.gestion_joueurs.ajouter_joueur(nouveau_joueur)
        self.gestion_joueurs.vue_joueur.afficher_message("Nouveau joueur ajouté avec succès !")
        return nouveau_joueur

