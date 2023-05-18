from tinydb import TinyDB, Query
from pathlib import Path


class SaveDB:
    def save_db(db_name, serialized_data):
        Path("./data/").mkdir(exist_ok=True)
        try:
            db = TinyDB(f"./data/{db_name}.json", indent=4)
        except FileNotFoundError:
            with open(f"./data/{db_name}.json", "w"):
                pass
            db = TinyDB("./data/" + db_name + ".json", indent=4)

        db.insert(serialized_data)







