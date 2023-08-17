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
                if self.gestion_joueurs:
                    self.gestion_joueurs.gerer_choix_utilisateur()
                else:
                    print("Erreur: La gestion des joueurs n'est pas configurée.")
            elif choix == "2":
                if self.gestion_tournoi:
                    self.gerer_tournois()
                else:
                    print("Erreur: La gestion des tournois n'est pas configurée.")
            elif choix == "3":
                print("Au revoir!")
                break
            else:
                print("Choix non reconnu. Veuillez choisir une option valide.")

    def gerer_tournois(self):
        while True:
            print("\nMenu tournoi:")
            print("1. Créer un tournoi")
            print("2. Reprendre la création d'un tournoi")
            print("3. Modifier un tournoi")
            print("4. Retour au menu principal")

            choix = input("Veuillez faire un choix : ")

            try:
                if choix == "1":
                    nom = input("Nom du tournoi : ")
                    lieu = input("Lieu du tournoi : ")
                    date_debut = input("Date de début (format YYYY-MM-DD) : ")
                    date_fin = input("Date de fin (format YYYY-MM-DD) : ")
                    nombre_tours = int(input("Nombre de tours (défaut: 4) : ") or 4)
                    description = input("Description du tournoi : ")
                    self.gestion_tournoi.creer_tournoi(nom, lieu, date_debut, date_fin, nombre_tours, description)

                elif choix == "2":
                    nom_tournoi = input("Entrez le nom du tournoi que vous souhaitez poursuivre : ")
                    tournoi = self.gestion_tournoi.charger_tournoi(nom_tournoi)
                    if tournoi:
                        print(f"Poursuite de la création du tournoi {tournoi.nom}")
                        # Suite de la logique ici
                    else:
                        print("Tournoi non trouvé.")

                elif choix == "3":
                    # Logique pour modifier le tournoi
                    pass

                elif choix == "4":
                    return

                else:
                    print("Choix non reconnu. Veuillez choisir une option valide.")

            except ValueError:
                print("Une erreur de valeur est survenue. Assurez-vous de saisir correctement les informations.")
