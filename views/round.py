class RoundView:
    def user_choice(self):
        user_input = input("\nSouhaitez-vous:\n"
                    "1 - Créer un nouveau round\n"
                    "2 - Entrer les scores du round en cours\n"
                    "3 - Modifier les informations d'un round\n"
                    "4 - Supprimer le round en cours\n"
                    "5 - Retourner en arrière\n")

        return user_input
    
    def custom_input(self, message):
        return input(message)
    
    def custom_print(self, message):
        return print(message)