from controllers.match import MatchController
from views.round import RoundView
from models.round import RoundModel
from models.match import MatchModel
from tinydb import TinyDB
from tinydb.operations import add
import random

db_players = TinyDB('db_players.json').table("players").all()
db_tournaments = TinyDB('database.json').table("tournaments")

class RoundController:
    def __init__(self, tournament_doc_id):
        self.view = RoundView()
        self.tournament_doc_id = tournament_doc_id
        self.tournament = db_tournaments.get(doc_id=self.tournament_doc_id)
        self.rounds_number = self.tournament["rounds"]
        self.current_round = self.tournament["current_round"]

    def display_menu(self):
        while True:
            user_input = self.view.user_choice()
            if user_input == "1":
                self.create_round()
            elif user_input == "2":
                self.resume_round()
            elif user_input == "3":
                self.update_round()
            elif user_input == "4":
                self.delete_round()
            elif user_input == "5":
                return
            else: 
                self.view.custom_print("Erreur de sélection, veuillez sélectionner une option valide.")
                self.display_menu()

    def pair_players(self):
        tournament_players = list(self.tournament["players"])
        tournament_current_round = self.tournament["current_round"]
        all_players_chessIds = [player['chess_id'] for player in tournament_players]
        all_paired_players = []

        #if(tournament_current_round == 0):
        while len(all_players_chessIds) > 0:
            randomized_pair = random.sample(all_players_chessIds, 2)
            all_players_chessIds.remove(randomized_pair[0])
            all_players_chessIds.remove(randomized_pair[1])  
            all_paired_players.append(randomized_pair)

        return all_paired_players

    def create_round(self):
        tournament = db_tournaments.get(doc_id=self.tournament_doc_id) ## needs to be up-to-date
        current_round = tournament["current_round"] + 1
        all_paired_players = self.pair_players()
        created_matches = []

        tournament.update({"current_round": current_round}, doc_ids=[self.tournament_doc_id])

        for index, paired_players in enumerate(all_paired_players):
            match = MatchModel(f"Match {index+1}", paired_players, "En cours")
            created_matches.append(match.serializer())

        if (tournament["current_round"] <= tournament["rounds"]):
            start_time, end_time = self.view.get_round_data()
            round = RoundModel(current_round,start_time,end_time,created_matches)
            db_tournaments.update({"current_round": current_round}, doc_ids=[self.tournament_doc_id])
            db_tournaments.update(add("rounds_list", [round.serializer()]), doc_ids=[self.tournament_doc_id])
            self.view.custom_print("Round créé.")

        else:
            self.view.custom_print("Vous avez atteint le nombre maximal de rounds pour ce tournoi.")

    def resume_round(self):
        MatchController(self.tournament["rounds"], self.tournament["current_round"], self.tournament["current_round"], self.tournament_doc_id).display_menu()
    
    def update_round(self):
        round_number = self.view.custom_input(f"Entrez le round à modifier ({self.current_round} sur {self.rounds_number})")
        MatchController(self.rounds_number, self.current_round, round_number, self.tournament_doc_id).display_menu()

    def delete_round(self):
        selected_round = self.view.custom_input(f"Entrez le round à supprimer ({self.current_round} sur {self.rounds_number}) : ")
        filtered_rounds = []

        for round in self.tournament["rounds_list"]:
            if round["round_number"] != int(selected_round):
                filtered_rounds.append(round)

        self.tournament["rounds_list"] = filtered_rounds
        db_tournaments.update(self.tournament, doc_ids=[self.tournament_doc_id])