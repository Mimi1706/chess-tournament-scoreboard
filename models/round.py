class RoundModel: 
    def __init__(self, round_number, start_time, end_time, matches):
        self.round_number = round_number
        self.start_time = start_time
        self.end_time = end_time
        self.matches = matches

    def serializer(self):
        round = {
            "round_number": self.round_number,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": self.matches
        }

        return round