# controllers/game_controller.py
from kivy.uix.screenmanager import ScreenManager


class GameController:
    def __init__(self, screen_manager: ScreenManager):
        self.screen_manager = screen_manager
        self.weapon_quantities = {}

    def start_game(self, level, bullets, bombshells, lasers):
        self.weapon_quantities = {
            'bullets': bullets,
            'bombshells': bombshells,
            'lasers': lasers
        }
        self.screen_manager.current = level

    def get_weapon_quantities(self):
        return self.weapon_quantities
