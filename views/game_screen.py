# game_screen.py
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('views/game_screen.kv')


class GameScreen(Screen):
    def start_new_game(self):
        self.manager.current = 'weapon_selection_screen'
