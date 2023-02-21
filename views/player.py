class View:
    def __init__(self):
        pass

    def get_player_data(self):
        first_name = input("Prénom : ")
        last_name = input("Nom de famille : ")
        birthdate = input("Date de naissance : ")
        chess_id = input("Identifiant national d'échecs : ")

        return first_name, last_name, birthdate, chess_id
    
    def user_choice(self):
        user_input = input("Souhaitez-vous:\n"
                    "1 - Créer un joueur\n"
                    "2 - Trouver un joueur\n"
                    "3 - Modifier un joueur\n"
                    "4 - Supprimer un joueur\n")
        
        return user_input
    
    def custom_input(self, message):
        return input(message)
    
    def custom_print(self, message):
        print(message)