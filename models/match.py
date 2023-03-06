class MatchModel:
    def __init__(self, name, paired_players):
        self.name = name
        self.player1 = paired_players[0]
        self.score_player1 = 0
        self.player2 = paired_players[1]
        self.score_player2 = 0
        self.score = [self.score_player1, self.score_player2]
        self.winner = ""

    def serializer(self):

        if (self.score_player1 > self.score_player2):
            self.winner=self.player1
        elif (self.score_player1 < self.score_player2):
            self.winner=self.player2
        elif(self.score_player1 == self.score_player2):
            self.winner= "\u00c9galit\u00e9"
    
        match = {
            "name": self.name,
            "player1": self.player1,
            "player2": self.player2,
            "score": f"J1: {self.score[0]} | J2: {self.score[1]}",
            "winner": self.winner
        }

        return match
        