from models.tournament import TournamentModel
from views.tournament import TournamentView
from controllers.round import RoundController
from tinydb import TinyDB, where

db_players = TinyDB('db_players.json').table("players").all()
db_tournaments = TinyDB('database.json').table("tournaments")

class TournamentController:
    def __init__(self):
        self.view = TournamentView()

    def display_menu(self):
        while True:
            user_input = self.view.user_choice()
            if user_input == "1":
                self.create_tournament()
            elif user_input == "2":
                self.resume_tournament()
            elif user_input == "4":
                self.delete_tournament()
            elif user_input == "5":
                return
            else:
                self.view.custom_print("Erreur de sélection, veuillez sélectionner une option valide.")
                self.display_menu()
                
    def create_tournament(self):
        name, location, start_date, end_date, rounds, notes = self.view.get_tournament_data()
        tournament = TournamentModel(name, location, start_date, end_date, db_players, notes, rounds, current_round=0, rounds_list=[])
        db_tournaments.insert(tournament.serializer())
        self.view.custom_print("Tournoi créé.")

    def resume_tournament(self):
        tournament_name = self.view.custom_input("Entrez le nom du tournoi à charger: ")
        if(db_tournaments.get(where("name") == tournament_name) == None):
            self.view.custom_print("Erreur, ce tournoi n'existe pas.")
            return
        
        else:
            selected_tournament = db_tournaments.get(where("name") == tournament_name)
            tournament_doc_id = selected_tournament.doc_id
            RoundController(tournament_doc_id).display_menu()
    
    def delete_tournament(self):
        tournament_name = self.view.custom_input("Entrez le nom du tournoi à effacer: ")
        if(db_tournaments.get(where("name") == tournament_name) == None):
            self.view.custom_print("Erreur, ce tournoi n'existe pas.")
            self.display_menu()
        else:
            db_tournaments.remove(where("name") == tournament_name)
            self.view.custom_print("Tournoi supprimé.")
           




        
