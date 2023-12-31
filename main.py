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

    # Boucle principale
    continuer = True
    while continuer:
        continuer = menu.afficher_menu_principal()

    # Fermez la base de données avant de quitter
    gestion_joueurs.fermer_db()

if __name__ == "__main__":
    main()
