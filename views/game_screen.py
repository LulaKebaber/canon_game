# game_screen.py
from kivy.uix.screenmanager import Screen

class GameScreen(Screen):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller

    def start_new_game(self):
        """Switches the screen and sets the selected level to 'level1' as default."""
        self.controller.selected_level = 'level1'
        self.manager.current = 'weapon_selection_screen'
    
    def select_level(self):
        """Switches the screen to the level selecting screen."""
        self.manager.current = 'select_level_screen'
