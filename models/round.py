class RoundModel: 
    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def serializer(self):
        round = {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
        }

        return round