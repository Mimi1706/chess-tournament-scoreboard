from controllers.match import MatchController
from views.round import RoundView
from models.round import RoundModel
from models.match import MatchModel
from tinydb import TinyDB
from tinydb.operations import add
from datetime import datetime

db_players = TinyDB("db_players.json").table("players").all()
db_tournaments = TinyDB("db_tournaments.json").table("tournaments")


class RoundController:
    def __init__(self, tournament_doc_id):
        self.current_time = datetime.now().strftime("%d/%m/%Y-%H:%M")
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
                return
            else:
                self.view.custom_print(
                    "Erreur de sélection, veuillez sélectionner une option valide."
                )
                self.display_menu()

    def pair_players(self):
        tournament = db_tournaments.get(doc_id=self.tournament_doc_id)
        descending_sorted_tournament_players = sorted(
            list(tournament["players"]), key=lambda p: p["score"], reverse=True
        )
        all_players_chessIds = [
            player["chess_id"] for player in descending_sorted_tournament_players
        ]
        already_paired_players = []
        next_round_paired_players = []
        for round in tournament["rounds_list"]:
            for match in round["matches"]:
                already_paired_players.append(match["players"])
        while len(all_players_chessIds) > 0:
            paired_players = all_players_chessIds[:2]
            if (
                paired_players in already_paired_players
                and len(all_players_chessIds) > 2
            ):
                paired_players = all_players_chessIds[1:3]
            all_players_chessIds.remove(paired_players[0])
            all_players_chessIds.remove(paired_players[1])
            next_round_paired_players.append(paired_players)
        return next_round_paired_players

    def create_round(self):
        message = "Veuillez entrer les scores des matchs du round en cours avant de pouvoir créer un nouveau round."
        tournament = db_tournaments.get(doc_id=self.tournament_doc_id)
        for round in tournament["rounds_list"]:
            for match in round["matches"]:
                if match["winner"] == "En cours":
                    self.view.custom_print(message)
                    return self.display_menu()
        all_paired_players = self.pair_players()
        created_matches = []
        for index, paired_players in enumerate(all_paired_players):
            match = MatchModel(f"Match {index+1}", paired_players, "En cours")
            created_matches.append(match.serializer())
        if tournament["current_round"] < tournament["rounds"]:
            next_round_number = tournament["current_round"] + 1
            round = RoundModel(
                next_round_number,
                created_matches,
                start_time=self.current_time,
                end_time="En cours",
            )
            db_tournaments.update(
                {"current_round": next_round_number}, doc_ids=[self.tournament_doc_id]
            )
            db_tournaments.update(
                add("rounds_list", [round.serializer()]),
                doc_ids=[self.tournament_doc_id],
            )
            self.view.custom_print("Round créé.")
        else:
            self.view.custom_print(
                "Vous avez atteint le nombre maximal de rounds pour ce tournoi."
            )

    def resume_round(self):
        tournament = db_tournaments.get(doc_id=self.tournament_doc_id)
        last_round_index = tournament["current_round"] - 1
        last_round = tournament["rounds_list"][last_round_index]
        if last_round["end_time"] == "En cours":
            MatchController(
                tournament["rounds"],
                tournament["current_round"],
                self.tournament_doc_id,
            ).display_menu()
        else:
            self.view.custom_print("Vous avez déjà entré les scores de ce round.")
            return self.display_menu()
