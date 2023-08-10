from Controller.menu import Menu
from Controller.gestion_joueur import GestionJoueurs  # Notez le "s" à "joueurs" pour correspondre au nom de fichier
from Controller.gestion_tournoi import GestionTournoi

def main():
    # Initialisation des contrôleurs
    gestion_joueurs = GestionJoueurs()
    gestion_tournoi = GestionTournoi()

    # Initialisation de la vue (Menu)
    menu = Menu()
    menu.set_gestion_joueurs(gestion_joueurs)
    menu.set_gestion_tournoi(gestion_tournoi)

    # Affichage du menu principal
    menu.afficher_menu_principal()

if __name__ == "__main__":
    main()