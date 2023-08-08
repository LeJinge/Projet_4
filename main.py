from Model.joueur import Joueur
from Vue.affichage_joueur import VueJoueur
from Controller.gestion_joueur import GestionJoueurs, CreationDeJoueur

if __name__ == "__main__":
    vue_joueur = VueJoueur()
    gestion_joueurs = GestionJoueurs()
    gestion_joueurs.set_vue(vue_joueur)

    creation_joueur = CreationDeJoueur(gestion_joueurs)
    nouveau_joueur = creation_joueur.creer_joueur_manuellement()

    gestion_joueurs.ajouter_joueur(nouveau_joueur)
