class VueJoueur:
    def afficher_message(self, message):
        print(message)

    def demander_information(self, texte):
        return input(texte)

    def afficher_menu(self):
        print("1. Créer un nouveau joueur")
        print("2. Supprimer un joueur existant")
        choix = input("Choisissez une option : ")
        return choix
