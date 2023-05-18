from models.match import Match

class Round:
    def __init__(self, name, players_pair):
        self.name = name
        self.players_pair = players_pair
        self.sort_players = []
        self.played_with = []
        self.matchs = []


    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.matchs}"

    def score_sorted_players(self):
        score_sorted_players_ = sorted(self.players_pair, key=lambda x: x.total_score, reverse=True)

        return score_sorted_players_

    def sorted_players(self, remaining_players=None):
        if remaining_players is None:
            remaining_players = self.score_sorted_players()
            self.played_with = []

        if not remaining_players:
            return []

        player1 = remaining_players[0]
        current_pairs = []

        for i in range(1, len(remaining_players)):
            player2 = remaining_players[i]
            if (player1, player2) not in self.played_with and (player2, player1) not in self.played_with:
                new_remaining_players = remaining_players[1:i] + remaining_players[i + 1:]
                current_pairs = [(player1, player2)] + self.sorted_players(new_remaining_players)
                self.played_with.extend([(player1, player2), (player2, player1)])
                break
        self.sort_players = current_pairs
        return self.sort_players

    def create_matchs(self):
        for i, pair in enumerate(self.sort_players):
            self.matchs.append(Match(name=f"Match {i}", players_pair=pair))
        return self.matchs


    def get_serialized_round(self):
        serialized_round = {
            "name": self.name,
            "matchs": [match.get_serialized_match() for match in self.matchs]
        }

        return serialized_round








