
class ViewPlayer:
    def create_player(self):
        name = input("Rentrez le nom du joueur \n >  ")
        firstname = input(f"Rentrez le prenom de {name} \n >  ")
        date_of_birth = input(f"Rentrez la date de naissance de {firstname} {name} \n >  ")

        print(f"Joueur Créé.")

        return {
            "name": name,
            "firstname": firstname,
            "date_of_birth": date_of_birth,
            }