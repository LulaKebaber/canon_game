# main_menu.py
from kivy.uix.screenmanager import Screen

class MainMenu(Screen):
    def start_game(self):
        """Switches the screen to the game screen."""
        self.manager.current = 'game_screen'

    def show_ranking(self):
        """Switches the screen to the ranking screen."""
        self.manager.current = 'ranking_screen'

    def show_help(self):
        """Switches the screen to the help screen."""
        self.manager.current = 'help_screen'
