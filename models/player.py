class PlayerModel:
    def  __init__(self, first_name, last_name, birthdate, chess_id, score=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.chess_id = chess_id
        self.score = score
    
    def serializer(self):
        player = {
            "first_name":self.first_name, 
            "last_name": self.last_name, 
            "birthdate": self.birthdate, 
            "chess_id": self.chess_id,
            "score": self.score
        }

        return player