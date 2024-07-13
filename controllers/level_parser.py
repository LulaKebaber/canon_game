import json


class LevelParser:
    def __init__(self, level=None):
        self.level = level
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open("data/levels.json") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("File data/levels.json not found.")
        except json.JSONDecodeError:
            raise ValueError("File data/levels.json contains invalid JSON.")
    
    def parse_level_info(self):
        try:
            levels = self.data["levels"]
            return levels.get(self.level, {})
        except KeyError:
            raise KeyError("The key 'levels' was not found in the JSON data.")
        
    def parse_obstacle_properties(self):
        return self.data["obstacles_properties"]
    
    def parse_targets_properties(self):
        return self.data["targets_properties"]
    
    def save_score(self, score, bullets_spent):
        with open("data/records.json", "r") as file:
            records = json.load(file)
            records["records"][str(len(records["records"]) + 1)] = {
                "id": len(records["records"]) + 1,
                "score": score,
                "bullets_spent": bullets_spent
            }
        with open("data/records.json", "w") as file:
            json.dump(records, file)
    
    def sort_records(self):
        try:
            with open("data/records.json") as file:
                records_data = json.load(file)
            
            records = list(records_data["records"].values())

            sorted_records = sorted(
                records,
                key=lambda record: (-record["score"], sum(record["bullets_spent"]))
            )

            sorted_records_dict = {str(i + 1): record for i, record in enumerate(sorted_records)}
            records_data["records"] = sorted_records_dict

            with open("data/records.json", "w") as file:
                json.dump(records_data, file, indent=4)

        except FileNotFoundError:
            raise FileNotFoundError("File data/records.json not found.")
        except json.JSONDecodeError:
            raise ValueError("File data/records.json contains invalid JSON.")
        except KeyError:
            raise KeyError("The key 'records' was not found in the JSON data.")
