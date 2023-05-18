from models.player import Player
from models.match import Match
from models.round import Round
from models.tournament import Tournament

from controller.controller_player import ControllerPlayer

#from controller.controller_round import ControllerRound
from controller.controller_tournament import ControllerTournament

from views.player import ViewPlayer
from views.match import ViewMatch
#from views.round import ViewRound
from views.tournament import ViewTournament





controller = ControllerTournament()
tournoi = controller.create_tournament()
print(tournoi.players)





















