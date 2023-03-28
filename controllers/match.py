from views.match import MatchView
from tinydb import TinyDB, Query

db_tournaments = TinyDB('database.json').table("tournaments")

Player = Query()

class MatchController:
    def __init__(self, rounds_number, current_round, round_number, tournament_doc_id):
        self.view = MatchView()
        self.rounds_number = rounds_number
        self.current_round = current_round
        self.round_number = round_number
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
        print(self.round_number)

        round = self.tournament["rounds_list"][self.round_number-1]
        matches = round[f'round_{self.round_number}']['matches']
    
        for match in matches:
            player1 = match["player1"]
            player2 = match["player2"]
            match_name = match["name"]
            print(f"\n{match_name} : J1({player1}) vs J2({player2})\n")
            user_input = self.view.get_match_scores()

            if(user_input == "1"): #P1 wins
                match["score"] = 'J1: 1 | J2: 0'
                match["winner"] = player1
                self.find_player(player1, 1)
            elif(user_input == "2"): #P2 wins
                match["score"] = 'J1: 0 | J2: 1'
                match["winner"] = player2
                self.find_player(player2, 1)
            elif(user_input == "3"): #Tie
                match["score"] = 'J1: 0,5 | J2: 0,5'
                match["winner"] = "Égalité"
                self.find_player(player1, 0.5)
                self.find_player(player2, 0.5)
            elif(user_input == "4"): 
                return
            else:
                print("Veuillez choisir une option valide")
                self.write_score()

        db_tournaments.update(self.tournament, doc_ids=[self.tournament_doc_id])
    
    def update_match(self):
        pass

    def delete_match(self):
        pass
