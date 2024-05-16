# controllers/game_controller.py
class GameController:
    def __init__(self, screen_manager, **kwargs):
        self.screen_manager = screen_manager
        self.bullets = 0
        self.bombshells = 0
        self.lasers = 0

    def start_game(self, level, bullets, bombshells, lasers):
        self.screen_manager.current = level
        self.bullets = bullets
        self.bombshells = bombshells
        self.lasers = lasers
