# models/player.py

class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def increase_score(self, points):
        self.score += points
