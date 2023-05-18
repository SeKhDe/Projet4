from views.player import ViewPlayer
class ViewTournament:
    def get_create_tournament(self):
        name = input(" Nom du tournoi \n >  ")
        place = input(" Lieu du tournoi \n >  ")
        date = input("date \n >  ")
        nb_players = input(" Nombre de joueur du tournoi  \n >  ")
        nb_rounds = input(" Nombre de tours du tournoi (4 par default) \n >  ")
        description = input(" Description du tournoi: \n >  ")

        return {
            "name": name,
            "place": place,
            "date": date,
            "nb_players": nb_players,

            "nb_rounds": nb_rounds,
            "description": description,
        }



