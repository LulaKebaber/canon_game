import json
import os


class LevelParser:
    def __init__(self, level):
        self.level = level
        self.data = None

    def parse_json(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "levels.json")
        with open(json_path) as file:
            self.data = json.load(file)

    def parse_targets(self):
        targets = self.data["targets"]
        return targets

    def parse_level(self):
        levels = self.data["levels"]
        return levels.get(self.level, {})
