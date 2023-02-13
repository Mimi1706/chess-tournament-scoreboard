class Tournament:
    def __init__(self, name, place, start_date, end_date, players, round_list, notes, rounds=4 ):
         self.name = name
         self.place = place
         self.start_date = start_date
         self.end_date = end_date
         self.players = players
         self.round_list = round_list
         self.notes = notes
         self.rounds = rounds