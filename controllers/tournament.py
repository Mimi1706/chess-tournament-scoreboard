from models.tournament import TournamentModel
from models.logs import LogsModel
from views.tournament import TournamentView
from views.player import PlayerView
from controllers.round import RoundController
from controllers.player import PlayerController
from tinydb import TinyDB, where

db_players = TinyDB('db_players.json').table("players").all()
db_tournaments = TinyDB('db_tournaments.json').table("tournaments")

class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.player_view = PlayerView()

    def display_menu(self):
        while True:
            user_input = self.view.user_choice()
            if user_input == "1":
                self.create_tournament()
            elif user_input == "2":
                self.resume_tournament()
            elif user_input == "3":
                self.update_tournament()
            elif user_input == "4":
                self.delete_tournament()
            elif user_input == "5":
                return
            else:
                self.view.custom_print("Erreur de sélection, veuillez sélectionner une option valide.")
                self.display_menu()
                
    def create_tournament(self):
        name, location, start_date, end_date, rounds, notes = self.view.get_tournament_data()
        players = []

        while True: 
            user_input = self.player_view.add_player()
            serialized_players = list(map(lambda player: player["chess_id"], players))
            self.view.custom_print(f"Joueurs inscrits : {serialized_players}")
            if user_input == "1":
                new_player = PlayerController().load_player()
                if new_player:
                    players.append(new_player)
            elif user_input == "2":
                deleted_player = PlayerController().load_player()
                if deleted_player:
                    players = list(filter(lambda player: (player['chess_id'] != deleted_player["chess_id"]), players))
            elif user_input == "3":
                tournament = TournamentModel(name, location, start_date, end_date, players, notes, rounds, current_round=0, rounds_list=[])
                db_tournaments.insert(tournament.serializer())
                return self.view.custom_print("Tournoi créé.")
            else:
                self.view.custom_print("Erreur de sélection, veuillez sélectionner une option valide.")
                self.player_view.add_player()

    def find_tournament(self):
        tournament_name = self.view.custom_input("Entrez le nom du tournoi à charger: ")
        if(db_tournaments.get(where("name") == tournament_name) == None):
            self.view.custom_print("Erreur, ce tournoi n'existe pas.")
            return self.display_menu()
        else:
            return db_tournaments.get(where("name") == tournament_name)

    def resume_tournament(self):
        selected_tournament = self.find_tournament()
        RoundController(selected_tournament.doc_id).display_menu()

    def update_tournament(self):
        selected_tournament = self.find_tournament()
        for input, info in zip(self.view.get_tournament_data(), selected_tournament):
            if input != "":
                selected_tournament[info] = input
        db_tournaments.update(selected_tournament, doc_ids=[selected_tournament.doc_id])
        self.view.custom_print("Modifications sauvegardées.")

    def delete_tournament(self):
        selected_tournament = self.find_tournament()
        db_tournaments.remove(where("name") == selected_tournament["name"])
        self.view.custom_print("Tournoi supprimé.")