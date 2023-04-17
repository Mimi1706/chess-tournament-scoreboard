class TournamentView:
    def get_tournament_data(self):
        name = input("Nom du tournoi : ")
        location = input("Emplacement du tournoi : ")
        start_date = input("Date de début du tournoi : ")
        end_date = input("Date de fin du tournoi : ")
        rounds = input("Nombre de rounds (Par défaut à 4) : ")
        notes = input("Notes à ajouter : ")

        if (rounds == ""):
            rounds = 4

        return name, location, start_date, end_date, int(rounds), notes

    def user_choice(self):
        user_input = input("\nSouhaitez-vous:\n"
                    "1 - Créer un nouveau tournoi\n"
                    "2 - Continuer un tournoi\n"
                    "3 - Modifier un tournoi\n"
                    "4 - Supprimer un tournoi\n"
                    "5 - Retourner en arrière\n")

        return user_input
    
    def custom_input(self, message):
        return input(message)
    
    def custom_print(self, message):
        return print(message)