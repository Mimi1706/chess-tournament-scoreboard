class Player:
    def __init__ (self, first_name, last_name, birthdate, chess_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.chess_id = chess_id

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

