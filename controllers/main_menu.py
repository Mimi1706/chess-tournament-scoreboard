from views.main_menu import MainMenuView
from controllers.tournament import TournamentController
from controllers.player import PlayerController
from controllers.logs import LogsController


class MainMenuController:
    def __init__(self):
        self.view = MainMenuView()

    def display_menu(self):
        while True:
            user_input = self.view.user_choice()
            if user_input == "1":
                TournamentController().display_menu()
            elif user_input == "2":
                PlayerController().display_menu()
            elif user_input == "3":
                LogsController().display_menu()
            elif user_input == "4":
                quit()
            else:
                self.view.custom_print(
                    "Erreur de sélection, veuillez sélectionner une option valide."
                )
                self.display_menu()
