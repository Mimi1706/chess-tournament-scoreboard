from views.logs import LogsView
from models.logs import LogsModel
from tinydb import TinyDB, where

db_tournaments = TinyDB('database.json').table("tournaments")
db_players = TinyDB('db_players.json').table("players")

class LogsController:
    def __init__(self):
        self.view = LogsView()

    def display_menu(self):
        while True:
            user_input = self.view.user_choice()
            if user_input == "1":
                self.show_all_players()
            elif user_input == "2":
                self.show_all_tournaments()
            elif user_input == "3":
                self.show_selected_tournament()
            elif user_input == "4":
                self.show_selected_tournament_players()
            elif user_input == "5":
                self.show_selected_tournament_matches()
            elif user_input == "6":
                return
            else: 
                self.view.custom_print("Erreur de sélection, veuillez sélectionner une option valide.")
                self.display_menu()

    def show_players(self, players):
        serialized_players = []
        for player in players:
            serialized_players.append(LogsModel.serialize_player(player))
        return serialized_players

    def show_rounds_matches(self, tournament):
        serialized_rounds = []
        for round in tournament["rounds_list"]:
            matches = []
            for match in round["matches"]:
                serialized_match = LogsModel.serialize_match(match)
                matches.append(serialized_match)
            serialized_rounds.append(LogsModel.serialize_round(round,matches))
        return serialized_rounds 

    def show_tournament(self, tournament):
        return self.view.custom_print(LogsModel.serialize_tournament(tournament, self.show_players(tournament["players"]), self.show_rounds_matches(tournament)))      

    def show_all_players(self):
        return self.view.custom_print_data(self.show_players(db_players))

    def show_all_tournaments(self):
        for tournament in db_tournaments:
            self.show_tournament(tournament)
                
    def selected_tournament(self):
        tournament_name = self.view.custom_input("Entrez le nom du tournoi à charger: ")
        selected_tournament = db_tournaments.get(where("name") == tournament_name)
        if (selected_tournament):
            return selected_tournament
        else:
            return self.view.custom_print("Erreur, ce tournoi n'existe pas.")

    def show_selected_tournament(self):
        selected_tournament = self.selected_tournament()
        return self.view.custom_print(self.show_tournament(selected_tournament))

    def show_selected_tournament_players(self):
        selected_tournament = self.selected_tournament()
        return self.view.custom_print(self.show_players(selected_tournament["players"]))

    def show_selected_tournament_matches(self):
        selected_tournament = self.selected_tournament()
        return self.view.custom_print(self.show_rounds_matches(selected_tournament))
    