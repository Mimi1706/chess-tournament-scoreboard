from views.match import MatchView

class MatchController:
    def __init__(self, current_round):
        self.view = MatchView()
        self.current_ = current_round

    def display_menu(self):
        while True:
            user_input = self.view.user_choice()

            if user_input == "1":
                self.write_score()

            elif user_input == "2":
                self.update_match()

            elif user_input == "3":
                self.delete_match()

            elif user_input == "4":
                return

            else: 
                self.view.custom_print("Erreur de sélection, veuillez sélectionner une option valide.")
                self.display_menu()

    def write_score(self):
        user_input = self.view.get_match_scores()

        if(user_input == "1"): #P1 wins
            pass
        elif(user_input == "2"): #P2 wins
            pass
        elif(user_input == "3"): #Tie
            pass
        else:
            print("Veuillez choisir une option valide")
            self.write_scores()

    def find_match(self):
        match_number = self.view.custom_input("Entrez le numéro du match:")
        return match_number
        
    def update_match(self):
        match = self.find_match()
        pass

    def delete_match(self):
        pass
