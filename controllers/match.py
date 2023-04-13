from views.match import MatchView
from tinydb import TinyDB

db_tournaments = TinyDB('database.json').table("tournaments")

class MatchController:
    def __init__(self, rounds_number, current_round, tournament_doc_id):
        self.view = MatchView()
        self.rounds_number = rounds_number
        self.current_round = current_round
        self.tournament_doc_id = tournament_doc_id
        self.tournament = db_tournaments.get(doc_id=self.tournament_doc_id)

    def display_menu(self):
        self.view.custom_print(f"\n\nRound {self.current_round} sur {self.rounds_number}")        
        while True:
            user_input = self.view.user_choice()
            if user_input == "1":
                self.write_score()
            elif user_input == "2":
                self.find_player()
            elif user_input == "3":
                self.delete_match()
            elif user_input == "4":
                return
            else: 
                self.view.custom_print("Erreur de sélection, veuillez sélectionner une option valide.")
                self.display_menu()
    
    def find_player(self, chess_id, score):
        players = self.tournament["players"]
        for player in players:
            if player["chess_id"] == chess_id:
                player["score"] = player["score"] + score

    def write_score(self):
        round = self.tournament["rounds_list"][self.current_round-1]
        matches = round['matches']
    
        for match in matches:
            player1 = match["players"][0]
            player2 = match["players"][1]
            match_name = match["name"]
            self.view.custom_print(f"\n{match_name} : J1({player1}) vs J2({player2})\n")
            user_input = self.view.get_match_scores()

            if(user_input == "1"): #P1 wins
                match["score"] = [{player1: 1}, {player2: 0}]
                match["winner"] = player1
                self.find_player(player1, 1)
            elif(user_input == "2"): #P2 wins
                match["score"] = [{player1: 0}, {player2: 1}]
                match["winner"] = player2
                self.find_player(player2, 1)
            elif(user_input == "3"): #Tie
                match["score"] = [{player1: 0.5}, {player2: 0.5}]
                match["winner"] = "Égalité"
                self.find_player(player1, 0.5)
                self.find_player(player2, 0.5)
            elif(user_input == "4"): 
                return
            else:
                self.view.custom_print("Veuillez choisir une option valide")
                self.write_score()

        db_tournaments.update(self.tournament, doc_ids=[self.tournament_doc_id])
    
    def update_match(self):
        pass

    def delete_match(self):
        pass
