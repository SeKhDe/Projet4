import random

class Match:
    def __init__(self, name, players_pair):
        self.name = name
        self.player1 = players_pair[0]
        self.player2 = players_pair[1]
        self.color_player1 = ""
        self.color_player2 = ""
        self.score_player1 = 0
        self.score_player2 = 0
        self.winner = ""

    def __repr__(self):
        return f"{(self.player1, self.score_player1,  self.player2, self.score_player2)}"

    def display_match(self):
        print(f"Match : {self.player1} vs {self.player2}")
        print(f" 1 > {self.player1} ")
        print(f" 2 > {self.player2}")
        print(f" 3 > égalité")

    def assign_color(self):
        if random.choice([True, False]):
            self.color_player1 = "Blanc"
            self.color_player2 = "Noir"
        else:
            self.color_player1 = "Noir"
            self.color_player2 = "Blanc"

    def create_match(self, score):
        self.assign_color()
        if score == "1":
            self.score_player1 = 1
            self.winner = self.player1
            self.player1.total_score += 1

        elif score == "2":
            self.score_player2 = 1
            self.winner = self.player2
            self.player2.total_score += 1

        elif score == "3":
            self.score_player1 = self.score_player2 = 0.5
            self.player1.total_score = self.player2.total_score= 0.5

        return f"{self.player1} ({self.color_player1}) {self.score_player1} -" \
               f" {self.player2} ({self.color_player2}) {self.score_player2}"

    def get_serialized_match(self):
        serialized = {
            "name": self.name,
            "player 1": self.player1,
            "player 2": self.player2,
            "score player 1": self.score_player1,
            "score player 2": self.score_player2,
        }

        return serialized