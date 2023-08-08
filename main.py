from Vue.affichage_joueur import VueJoueur
from Controller.gestion_joueur import GestionJoueurs, CreationDeJoueur

if __name__ == "__main__":
    vue_joueur = VueJoueur()
    gestion_joueurs = GestionJoueurs()
    gestion_joueurs.set_vue(vue_joueur)

    choix = ""
    while choix != "q":
        choix = gestion_joueurs.gerer_choix_utilisateur()