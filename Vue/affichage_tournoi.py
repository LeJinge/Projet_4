class AffichageTournoi:
    def afficher_infos_tournoi(self, tournoi):
        print(f"Nom du tournoi: {tournoi.nom}")
        print(f"Lieu: {tournoi.lieu}")
        print(f"Date de début: {tournoi.date_debut}")
        print(f"Date de fin: {tournoi.date_fin}")