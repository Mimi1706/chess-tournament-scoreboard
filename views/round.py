class RoundView:
    def get_round_data(self):
        start_time = input("Horaire de début : ")
        end_time = input("Horaire de fin : ")
        return start_time, end_time

    def user_choice(self):
        user_input = input("\nSouhaitez-vous:\n"
                    "1 - Créer un round\n"
                    "2 - Continuer un round\n"
                    "3 - Supprimer un round\n"
                    "4 - Retourner en arrière\n")

        return user_input
    
    def custom_input(self, message):
        return input(message)
    
    def custom_print(self, message):
        return print(message)