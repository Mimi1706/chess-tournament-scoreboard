class MainMenuView:
    def user_choice(self):
        user_input = input(
            "\nBonjour, souhaitez-vous:\n"
            "1 - Gérer les tournois\n"
            "2 - Gérer la base de données de joueurs\n"
            "3 - Consulter les rapports\n"
            "4 - Quitter\n"
        )

        return user_input

    def custom_input(self, message):
        return input(message)

    def custom_print(self, message):
        return print(message)
