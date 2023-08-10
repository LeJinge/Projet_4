class AffichageJoueur:
    def afficher_message(self, message):
        print(message)

    def demander_information(self, texte):
        return input(texte)

    def afficher_menu(self):
        print("\nMenu gestion des joueurs:")
        print("1. Ajouter un joueur")
        print("2. Supprimer un joueur")
        print("3. Modifier un joueur")
        print("4. Retour au menu principal")

        choix = input("Veuillez faire un choix : ")
        return choix
