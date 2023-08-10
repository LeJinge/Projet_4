import json
from Model.joueur import Joueur
from Vue.affichage_joueur import AffichageJoueur

class GestionJoueurs:
    def __init__(self):
        self.gestion_joueurs = None
        self.donnees = self.charger_donnees()
        self.vue_joueur = AffichageJoueur()

    def charger_donnees(self):
        try:
            with open("joueurs.json", "r", encoding="utf-8") as fichier:
                data = json.load(fichier)
                print(data)
                return data
        except FileNotFoundError:
            return []

    def joueur_existe(self, nouveau_joueur):
        for joueur in self.donnees:
            if joueur["nom"] == nouveau_joueur.nom and joueur["prenom"] == nouveau_joueur.prenom:
                return True
        return False

    def ajouter_joueur(self, nouveau_joueur):
        if self.joueur_existe(nouveau_joueur):
            self.vue_joueur.afficher_message("Ce joueur existe déjà dans la liste, doublon non ajouté.")
        else:
            self.donnees.append(vars(nouveau_joueur))
            self.sauvegarder_donnees()
            self.vue_joueur.afficher_message("Nouveau joueur ajouté avec succès !")

    def sauvegarder_donnees(self):
        with open("joueurs.json", "w", encoding="utf-8") as fichier:
            json.dump(self.donnees, fichier, indent=4, ensure_ascii=False)

    def set_vue(self, vue_joueur):
        self.vue_joueur = vue_joueur

    def gerer_choix_utilisateur(self):
        while True:
            choix = self.vue_joueur.afficher_menu()

            if choix == "1":
                nouveau_joueur = self.creer_joueur_manuellement()  # crée un nouveau joueur
                self.ajouter_joueur(nouveau_joueur)
            elif choix == "2":
                self.supprimer_joueur()
            elif choix == "3":
                self.modifier_joueur()
            elif choix == "4":
                return  # Retour au menu principal
            else:
                print("Choix non reconnu. Veuillez choisir une option valide.")

    def modifier_joueur(self):
        # Étape 1: Demande du nom et prénom du joueur à l'utilisateur
        nom = input("Entrez le nom du joueur que vous souhaitez modifier : ")
        prenom = input("Entrez le prénom du joueur que vous souhaitez modifier : ")

        # Étape 2: Chargement des données depuis le fichier joueurs.json
        joueurs = []
        try:
            with open("joueurs.json", "r", encoding="utf-8") as fichier:
                data = json.load(fichier)
                joueurs = data
        except FileNotFoundError:
            print("Erreur : Fichier joueurs.json non trouvé.")
            return

        # Étape 3: Recherche du joueur dans la liste
        joueur_trouve = None
        for joueur in joueurs:
            if joueur['nom'] == nom and joueur['prenom'] == prenom:
                joueur_trouve = joueur
                break

        if not joueur_trouve:
            print("Erreur : Le joueur n'a pas été trouvé.")
            return

        # Étape 4: Lancement du processus de création pour obtenir les nouvelles informations
        print("Entrez les nouvelles informations pour le joueur:")
        nouveau_nom = input("Nom : ")
        nouveau_prenom = input("Prénom : ")
        nouvelle_date_naissance = input("Date de naissance (format YYYY-MM-DD) : ")
        # ... [Continuez pour d'autres champs si nécessaire]

        # Étape 5: Remplacement des anciennes données par les nouvelles
        joueur_trouve["nom"] = nouveau_nom
        joueur_trouve["prenom"] = nouveau_prenom
        joueur_trouve["date_de_naissance"] = nouvelle_date_naissance
        # ... [Continuez pour d'autres champs si nécessaire]

        # Étape 6: Sauvegardez les modifications dans le fichier joueurs.json
        with open("joueurs.json", "w", encoding="utf-8") as fichier:
            json.dump({"joueurs": joueurs}, fichier, ensure_ascii=False, indent=4)

        print("Le joueur a été modifié avec succès.")

    def supprimer_joueur(self):
        nom_a_effacer = self.vue_joueur.demander_information("Entrez le nom du joueur à effacer : ")
        prenom_a_effacer = self.vue_joueur.demander_information("Entrez le prénom du joueur à effacer : ")

        joueurs = self.donnees
        joueur_trouve = False

        for joueur in joueurs:
            if joueur["nom"] == nom_a_effacer and joueur["prenom"] == prenom_a_effacer:
                joueurs.remove(joueur)
                joueur_trouve = True
                break

        if joueur_trouve:
            self.sauvegarder_donnees()
            self.vue_joueur.afficher_message("Joueur supprimé avec succès !")
        else:
            self.vue_joueur.afficher_message("Joueur non trouvé.")

    def creer_joueur_manuellement(self):
        prenom = self.vue_joueur.demander_information("Entrez le prénom du joueur : ")
        nom = self.vue_joueur.demander_information("Entrez le nom du joueur : ")
        date_de_naissance = self.vue_joueur.demander_information("Entrez la date de naissance du joueur : ")

        nouveau_joueur = Joueur(nom, prenom, date_de_naissance)
        self.ajouter_joueur(nouveau_joueur)
        return nouveau_joueur

