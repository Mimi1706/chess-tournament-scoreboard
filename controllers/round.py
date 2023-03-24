from controllers.match import MatchController
from views.round import RoundView
from models.round import RoundModel
from models.match import MatchModel
from tinydb import TinyDB, where
from tinydb.operations import add
import random

db_players = TinyDB('db_players.json').table("players").all()
db_tournaments = TinyDB('database.json').table("tournaments")

class RoundController:
    def __init__(self, tournament_doc_id):
        self.view = RoundView()
        self.tournament_doc_id = tournament_doc_id
        self.tournament = db_tournaments.get(doc_id=self.tournament_doc_id)

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
        uptodate_tournament = db_tournaments.get(doc_id=self.tournament_doc_id)
        current_round = uptodate_tournament["current_round"] + 1
        all_paired_players = self.pair_players()
        created_matches = []
        start_time, end_time = self.view.get_round_data()
        round = RoundModel(current_round,start_time,end_time,created_matches)

        uptodate_tournament.update({"current_round": current_round}, doc_ids=[self.tournament_doc_id])

        for index, paired_players in enumerate(all_paired_players):
            match = MatchModel(f"Match_{index+1}", paired_players, "En cours")
            created_matches.append(match.serializer())

        if (uptodate_tournament["current_round"] <= uptodate_tournament["rounds"]):
            db_tournaments.update({"current_round": current_round}, doc_ids=[self.tournament_doc_id])
            db_tournaments.update(add("rounds_list", [{f"round_{current_round}":round.serializer()}]), doc_ids=[self.tournament_doc_id])
            print("Round créé.")

        else:
            self.view.custom_print("Vous avez atteint le nombre maximal de rounds pour ce tournoi.")

    def resume_round(self):
        current_round = self.tournament["current_round"]
        MatchController(current_round - 1).display_menu()
    
    def update_round(self):
        pass

        tournaments = db_tournaments.search(where("name")=="test")[0]
        current_match = self.create_round()
        all_matches = list(tournaments.get("rounds_list"))
        all_matches.extend(current_match)

        db_tournaments.update({"current_round":1}, doc_ids=[self.tournament_doc_id])
        db_tournaments.update({"rounds_list":all_matches}, doc_ids=[self.tournament_doc_id])

    def delete_round(self):
        pass