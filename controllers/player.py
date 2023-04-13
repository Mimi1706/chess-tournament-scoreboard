from models.player import PlayerModel
from views.player import PlayerView
from tinydb import TinyDB, where

db_players = TinyDB('db_players.json').table("players")

class PlayerController:
    def __init__(self):
        self.view = PlayerView()

    def display_menu(self):
        while True:
            user_input = self.view.user_choice()
            if user_input == "1":
                self.create_player()
            elif user_input == "2":
                self.load_player()
            elif user_input == "3":
                self.update_player()
            elif user_input == "4":
                self.delete_player()
            elif user_input == "5":
                return
            else: 
                self.view.custom_print("Erreur de sélection, veuillez sélectionner une option valide.")
                self.display_menu()

    def create_player(self):
        first_name, last_name, birthdate, chess_id = self.view.get_player_data()
        player = PlayerModel(first_name, last_name, birthdate, chess_id)
        db_players.insert(player.serializer())
        self.view.custom_print("Joueur créé.")

    def load_player(self):
        chess_id_input = self.view.custom_input("Quel l'identifiant national d'échecs du joueur ? ")
        player = db_players.search(where("chess_id") == chess_id_input)

        if player == []:
            return self.view.custom_print("Joueur non existant.")
        
        else:
            self.view.custom_print(player)

    def update_player(self):
        chess_id_input = self.view.custom_input("Quel l'identifiant national d'échecs du joueur ? ")
        player = db_players.search(where("chess_id") == chess_id_input)

        if player == []:
            return self.view.custom_print("Joueur non existant.")
        
        else:
            first_name = input("Prénom : ")
            last_name = input("Nom de famille : ")
            birthdate = input("Date de naissance : ")
            db_players.update({"first_name":first_name, "last_name": last_name, "birthdate": birthdate}, where("chess_id") == chess_id_input)
            self.view.custom_print("Joueur modifié.")

    def delete_player(self):
        chess_id_input = self.view.custom_input("Quel l'identifiant national d'échecs du joueur ? ")
        player = db_players.search(where("chess_id") == chess_id_input)

        if player == []:
            self.view.custom_print("Joueur non existant.")
        
        else:
            db_players.remove(where("chess_id") == chess_id_input)
            self.view.custom_print("Joueur supprimé.")

