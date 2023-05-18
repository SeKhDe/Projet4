import random
from tinydb import TinyDB, Query
from pathlib import Path

from controller.controller_player import ControllerPlayer

from views.tournament import ViewTournament
from models.tournament import Tournament
from views.player import ViewPlayer
from models.player import Player
from models.round import Round
from models.database import SaveDB



from models.match import Match
from views.match import ViewMatch


class ControllerTournament:
    def create_tournament(self):
        players = []
        user_input = ViewTournament().get_create_tournament()
        print("Création des joueurs")
        for i in range(int(user_input["nb_players"])):
            player = self.create_player()

            players.append(player)
        print(players)


        self.tournament = Tournament(
            user_input["name"],
            user_input["place"],
            user_input["date"],

            user_input["nb_players"],
            players,
            user_input["nb_rounds"],
            user_input["description"]
            )
        serialized_tournament = self.tournament.get_serialized_tournament()
        SaveDB.save_db(db_name="tournament", serialized_data=serialized_tournament)

        return self.tournament

    def create_player(self):

        player = ControllerPlayer.create_player()

        return player



    def create_round(self):
        players = self.tournament.players

        for i in range(int(self.tournament.nb_rounds)):
            print(f"Round {i+1}")
            rounds = Round(f"Round {i+1}", players)
            rounds.sorted_players()
            round = rounds.create_matchs()
            self.tournament.rounds.append(round)
            self.play_match(round)



    def play_match(self, matchs):
        for match in matchs:

            print(match)
            print(f"{match.player1} - {match.player2}")
            choice = ViewMatch.get_info()
            match.create_match(choice)
            self.tournament.matchs.append(match)
            m = input("match suivant >  ")


    def create_rank(self):
        rank = sorted(self.tournament.players, key=lambda x: x.total_score, reverse=True)
        self.tournament.add_rank(rank)



















