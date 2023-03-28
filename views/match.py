class MatchView: 
    def get_match_scores(self):
        user_input = input("Résultat du match:\n"
                    "1 - Victoire du Joueur 1\n"
                    "2 - Victoire du Joueur 2\n"
                    "3 - Égalité\n"
                    "4 - Quitter\n")

        return user_input

    def user_choice(self):
        user_input = input("\nSouhaitez-vous:\n"
                    "1 - Entrer les scores des matchs\n"
                    "2 - Modifier le score d'un match\n"
                    "3 - Supprimer un match\n"
                    "4 - Retourner en arrière\n")
    
        return user_input
    
    def custom_input(self, message):
        return input(message)
    
    def custom_print(self, message):
        return print(message)