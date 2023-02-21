from models.player import Player
from views.player import View
from tinydb import TinyDB, where

db = TinyDB('players.json')
players = db.table("players")

class Controller:
    def __init__(self):
        self.view = View()

    def display_menu(self):
        while True:
            user_input = self.view.user_choice()
            
            if user_input == "1":
                self.create_player()
                break

            elif user_input == "2":
                self.load_player()
                break

            elif user_input == "3":
                self.update_player()
                break

            elif user_input == "4":
                self.delete_player()
                break

            else: 
                print("Erreur de sélection, veuillez sélectionner une option valide.")

    def create_player(self):
        first_name, last_name, birthdate, chess_id = self.view.get_player_data()

        player = Player(first_name, last_name, birthdate, chess_id)

        players.insert(player.serializer())
        print("Joueur créé.")
        

    def load_player(self):
        chess_id_input = self.view.custom_input("Quel est votre identifiant national d'échecs ? ")
        player = players.search(where("chess_id") == chess_id_input)

        if player == []:
            self.view.custom_print("Joueur non existant.")
        
        else:
            self.view.custom_print(player)

    def update_player(self):
        chess_id_input = self.view.custom_input("Quel est votre identifiant national d'échecs ? ")
        player = players.search(where("chess_id") == chess_id_input)

        if player == []:
            print("Joueur non existant.")
        
        else:
            first_name = input("Prénom : ")
            last_name = input("Nom de famille : ")
            birthdate = input("Date de naissance : ")

            players.update({"first_name":first_name, "last_name": last_name, "birthdate": birthdate}, where("chess_id") == chess_id_input)
            print("Joueur modifié.")

    def delete_player(self):
        chess_id_input = self.view.custom_input("Quel est votre identifiant national d'échecs ? ")
        player = players.search(where("chess_id") == chess_id_input)

        if player == []:
            print("Joueur non existant.")
        
        else:
            players.remove(where("chess_id") == chess_id_input)
            print("Joueur supprimé.")

