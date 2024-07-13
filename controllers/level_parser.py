import json
import os

class LevelParser:
    def __init__(self, level):
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
    
    
