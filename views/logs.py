class LogsView:
    def user_choice(self):
        user_input = input("\nSouhaitez-vous consulter:\n"
                    "1 - La liste de tous les joueurs\n"
                    "2 - La liste de tous les tournois\n" 
                    "3 - Un tournoi en particulier\n"
                    "4 - La liste des joueurs d'un tournoi\n"
                    "5 - Les tours et matchs d'un tournoi\n"
                    "6 - Retour en arrière\n")
        
        return user_input
    
    def custom_input(self, message):
        return input(message)
    
    def custom_print(self, message):
        return print(message)

    def custom_print_break(self, match):
        print("")
        for match_info in match:
            print(f"{match_info} : {match[match_info]}")