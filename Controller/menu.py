class Menu:
    def __init__(self):
        self.gestion_joueurs = None
        self.gestion_tournoi = None

    def set_gestion_joueurs(self, gestion_joueurs):
        self.gestion_joueurs = gestion_joueurs

    def set_gestion_tournoi(self, gestion_tournoi):
        self.gestion_tournoi = gestion_tournoi

    def demander_choix_menu_principal(self):
        print("\nMenu principal:")
        print("1. Gérer les joueurs")
        print("2. Gérer les tournois")
        print("3. Quitter")
        choix = input("Veuillez faire un choix : ")
        return choix

    def afficher_menu_principal(self):
        while True:
            choix = self.demander_choix_menu_principal()

            if choix == "1":
                self.gestion_joueurs.gerer_choix_utilisateur()
            elif choix == "2":
                self.gerer_tournois()
            elif choix == "3":
                print("Au revoir!")
                break
            else:
                print("Choix non reconnu. Veuillez choisir une option valide.")

    def gerer_tournois(self):
        while True:
            print("\nMenu tournoi:")
            print("1. Créer un tournoi")
            print("2. Reprendre la création du tournoi en cours")
            print("3. Modifier un tournoi")
            print("4. Retour au menu principal")

            choix = input("Veuillez faire un choix : ")

            if choix == "1":
                nom = input("Nom du tournoi : ")
                lieu = input("Lieu du tournoi : ")
                date_debut = input("Date de début (format YYYY-MM-DD) : ")
                date_fin = input("Date de fin (format YYYY-MM-DD) : ")
                nombre_tours = int(input("Nombre de tours (défaut: 4) : ") or 4)
                description = input("Description du tournoi : ")
                self.gestion_tournoi.creer_tournoi(nom, lieu, date_debut, date_fin, nombre_tours, description)
            elif choix == "2":
                # Ajoutez la logique ou la méthode pour modifier les joueurs.
                pass  # Pour l'instant, c'est un espace réservé.
            elif choix == "3":
                # Ajoutez la logique ou la méthode pour supprimer les joueurs.
                pass  # Pour l'instant, c'est un espace réservé.
            elif choix == "4":
                self.gestion_tournoi.afficher_infos_tournoi()
            elif choix == "5":
                return  # retourner au menu principal
            else:
                print("Choix non reconnu. Veuillez choisir une option valide.")