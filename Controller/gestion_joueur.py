from tinydb import TinyDB, Query
from Model.joueur import Joueur
from Vue.affichage_joueur import AffichageJoueur
from tinydb.storages import JSONStorage

class GestionJoueurs:
    def __init__(self):
        self.db = TinyDB('joueurs.json', storage=JSONStorage, encoding='utf-8')
        self.table_joueurs = self.db.table('joueurs')
        self.vue_joueur = AffichageJoueur()
        self.JoueurQuery = Query()

    def joueur_existe(self, nom, prenom):
        joueur_dict = self.db.get((self.JoueurQuery.nom == nom) & (self.JoueurQuery.prenom == prenom))
        return bool(joueur_dict)

    def ajouter_joueur(self, joueur):
        print("Méthode ajouter_joueur appelée.")  # Debug
        if self.joueur_existe(joueur.nom, joueur.prenom):
            print("Joueur trouvé, doublon détecté.")  # Debug
            self.vue_joueur.afficher_message("Ce joueur existe déjà dans la liste, doublon non ajouté.")
        else:
            try:
                self.db.insert({
                    'nom': joueur.nom,
                    'prenom': joueur.prenom,
                    'date_de_naissance': joueur.date_de_naissance,
                    'identifiant_echec': joueur.identifiant_echec
                })
                self.vue_joueur.afficher_message("Nouveau joueur ajouté avec succès !")
            except Exception as e:
                print("Erreur lors de l'insertion:", e)

    def set_vue(self, vue_joueur):
        self.vue_joueur = vue_joueur

    def gerer_choix_utilisateur(self):
        while True:
            choix = self.vue_joueur.afficher_menu()

            if choix == "1":
                nouveau_joueur = self.creer_joueur_manuellement()
                self.ajouter_joueur(nouveau_joueur)
            elif choix == "2":
                self.supprimer_joueur()
            elif choix == "3":
                self.modifier_joueur()
            elif choix == "4":
                return
            else:
                print("Choix non reconnu. Veuillez choisir une option valide.")

    def modifier_joueur(self):
        nom = input("Entrez le nom du joueur que vous souhaitez modifier : ")
        prenom = input("Entrez le prénom du joueur que vous souhaitez modifier : ")
        identifiant = input("Entrez l'Identifiant National d'échec du joueur que vous souhaitez modifier : ")

        joueur_trouve = self.db.get(
            (self.JoueurQuery.nom == nom) &
            (self.JoueurQuery.prenom == prenom) &
            (self.JoueurQuery.identifiant_echec == identifiant)
        )

        if not joueur_trouve:
            print("Erreur : Le joueur n'a pas été trouvé.")
            return

        print("Entrez les nouvelles informations pour le joueur:")
        nouveau_nom = input("Nom : ")
        nouveau_prenom = input("Prénom : ")
        nouvelle_date_naissance = input("Date de naissance (format YYYY-MM-DD) : ")
        nouvel_identifiant = input("Nouvel Identifiant National d'échec : ")

        self.db.update({
            "nom": nouveau_nom,
            "prenom": nouveau_prenom,
            "date_de_naissance": nouvelle_date_naissance,
            "identifiant_echec": nouvel_identifiant
        }, (self.JoueurQuery.nom == nom) & (self.JoueurQuery.prenom == prenom) & (
                    self.JoueurQuery.identifiant_echec == identifiant))

        print("Le joueur a été modifié avec succès.")

    def supprimer_joueur(self):
        nom_a_effacer = input("Entrez le nom du joueur à effacer : ")
        prenom_a_effacer = input("Entrez le prénom du joueur à effacer : ")
        identifiant_a_effacer = input("Entrez l'Identifiant National d'échec du joueur à effacer : ")

        removed_count = self.db.remove(
            (self.JoueurQuery.nom == nom_a_effacer) &
            (self.JoueurQuery.prenom == prenom_a_effacer) &
            (self.JoueurQuery.identifiant_echec == identifiant_a_effacer)
        )

        if removed_count:
            self.vue_joueur.afficher_message("Joueur supprimé avec succès !")
        else:
            self.vue_joueur.afficher_message("Joueur non trouvé.")

    def creer_joueur_manuellement(self):
        prenom = input("Entrez le prénom du joueur : ")
        nom = input("Entrez le nom du joueur : ")
        date_de_naissance = input("Entrez la date de naissance du joueur : ")
        identifiant_echec = input("Entrez l'Identifiant National d'échec du joueur : ")

        nouveau_joueur = Joueur(nom, prenom, date_de_naissance, identifiant_echec)
        return nouveau_joueur

    def recuperer_joueur(self, nom=None, prenom=None, identifiant_echec=None):
        # S'assurer que soit le nom et prénom, soit l'identifiant sont fournis
        if not (nom and prenom) and not identifiant_echec:
            raise ValueError("Doit fournir soit (nom et prénom) soit identifiant_echec pour récupérer un joueur.")

        # Recherche par identifiant
        if identifiant_echec:
            joueur_dict = self.db.get(self.JoueurQuery.identifiant_echec == identifiant_echec)

        # Recherche par nom et prénom
        else:
            joueur_dict = self.db.get((self.JoueurQuery.nom == nom) & (self.JoueurQuery.prenom == prenom))

        if joueur_dict:
            # Convertir le dictionnaire en un objet Joueur
            return Joueur(
                joueur_dict['nom'],
                joueur_dict['prenom'],
                joueur_dict['date_de_naissance'],
                joueur_dict.get('identifiant_echec', None)
            )
        else:
            return None

    def fermer_db(self):
        self.db.close()