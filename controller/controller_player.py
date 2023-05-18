from views.player import ViewPlayer
from models.player import Player
from tinydb import TinyDB, Query
from pathlib import Path

from models.database import SaveDB

class ControllerPlayer:
    def create_player():

        user_entry = ViewPlayer().create_player()

        player = Player(
            user_entry["name"],
            user_entry["firstname"],
            user_entry["date_of_birth"]
        )
        seriarilized_player = player.get_serialized_player()


        SaveDB.save_db(db_name="player", serialized_data=seriarilized_player)
        return player


