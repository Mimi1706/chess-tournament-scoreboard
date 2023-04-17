from views.logs import LogsView
from models.logs import LogsModel
from tinydb import TinyDB, where

db_tournaments = TinyDB('db_tournaments.json').table("tournaments")
db_players = TinyDB('db_players.json').table("players")

class LogsController:
    def __init__(self):
        self.view = LogsView()

    def display_menu(self):
        while True:
            user_input = self.view.user_choice()
            if user_input == "1":
                self.show_players_database()
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

    def tournament_players(self, players):
        alphabetically_sorted_players = sorted(list(players), key=lambda p: p['last_name'])
        serialized_players = []
        for player in alphabetically_sorted_players:
            serialized_players.append(LogsModel.serialize_player(player))
        return serialized_players

    def tournament_rounds_matches(self, tournament):
        serialized_rounds = []
        for round in tournament["rounds_list"]:
            matches = []
            for match in round["matches"]:
                serialized_match = LogsModel.serialize_match(match)
                matches.append(serialized_match)
            serialized_rounds.append(LogsModel.serialize_round(round,matches))
        return serialized_rounds 

    def show_tournament(self, tournament):
        players = self.tournament_players(tournament["players"])
        rounds_matches = self.tournament_rounds_matches(tournament)
        return self.view.custom_print_break(LogsModel.serialize_tournament(tournament, players, rounds_matches))      

    def show_players_database(self):
        for player in self.tournament_players(db_players):
            self.view.custom_print(player)

    def show_all_tournaments(self):
        for tournament in db_tournaments:
            tournament_name = tournament["name"]
            tournament_start_date = tournament["start_date"]
            tournament_end_date = tournament["end_date"]
            self.view.custom_print(f"Nom du tournoi : {tournament_name} (du {tournament_start_date} au {tournament_end_date})")      
                
    def selected_tournament(self):
        tournament_name = self.view.custom_input("Entrez le nom du tournoi à charger: ")
        selected_tournament = db_tournaments.get(where("name") == tournament_name)
        if (selected_tournament):
            return selected_tournament
        else:
            self.view.custom_print("Erreur, ce tournoi n'existe pas.")
            return self.display_menu()
        
    def show_selected_tournament(self):
        selected_tournament = self.selected_tournament()
        self.view.custom_print(self.show_tournament(selected_tournament))

    def show_selected_tournament_players(self):
        selected_tournament = self.selected_tournament()
        players = self.tournament_players(selected_tournament["players"])
        for player in players:
            self.view.custom_print(player)

    def show_selected_tournament_matches(self):
        selected_tournament = self.selected_tournament()
        rounds_number = selected_tournament["rounds"]
        for round in selected_tournament["rounds_list"]:
            round_number = round["round_number"]
            self.view.custom_print(f"\nRound {round_number} sur {rounds_number}")
            for match in round["matches"]:
                self.view.custom_print_break(LogsModel.serialize_match(match))
    