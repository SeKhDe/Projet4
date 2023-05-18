from models.round import Round
from models.player import Player

class Tournament:
    def __init__(self, name, place, date, nb_players, players, nb_rounds=4, description=""):
        self.name = name
        self.place = place
        self.date = date
        self.nb_players = nb_players
        self.players = players
        self.nb_rounds = nb_rounds
        self.rounds = []
        self.description = description
        self.matchs = []
        self.ranks = []

    def __str__(self):
        return f"Tournoi {self.name}"




    def add_round(self, round):
        self.rounds.append(round)


    def add_player(self, player):
        self.players.append(player)


    def add_match(self, match):
        self.matchs.append(match)


    def add_rank(self, rank):
        self.ranks = rank

    def display_rank(self):
        print(" --- classement ---")
        for i, player in enumerate(self.ranks):
            print(f">  {i+1} - {player}")


    def get_serialized_tournament(self):
        serialized_tournament = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "nombre de joueurs": self.nb_players,
            "description": self.description,
            "Joueurs":[ player.get_serialized_player()
                for player in self.players] ,
        }

        return serialized_tournament












    
