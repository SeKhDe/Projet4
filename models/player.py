class Player:
    def __init__(self, name, firstname, date_of_birth):
        self.name = name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.rank = 0
        self.total_score = 0
        self.score_tournament = 0


    def __str__(self):
        return f"{self.name} {self.firstname}"

    def __repr__(self):
        return str(self)

    def get_serialized_player(self):
        serialized_player = {
            "name": self.name,
            "firstname": self.firstname,
            "date_of_birth": self.date_of_birth,
            "total_score": self.total_score,
            "rank": self.rank,
        }

        return serialized_player



