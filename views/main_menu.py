# main_menu.py
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('views/main_menu.kv')


class MainMenu(Screen):
    def start_game(self):
        self.manager.current = 'game_screen'

    def show_ranking(self):
        self.manager.current = 'ranking_screen'
