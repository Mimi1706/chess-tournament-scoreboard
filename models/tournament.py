class TournamentModel:
    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        players,
        notes,
        rounds,
        current_round,
        rounds_list,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.notes = notes
        self.rounds = rounds
        self.current_round = current_round
        self.rounds_list = rounds_list

    def serializer(self):
        tournament = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "players": self.players,
            "notes": self.notes,
            "rounds": self.rounds,
            "current_round": self.current_round,
            "rounds_list": self.rounds_list,
        }

        return tournament
