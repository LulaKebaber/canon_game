# views/end_game_screen.py
from kivy.uix.screenmanager import Screen


class EndGameScreen(Screen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
    
    def on_restart_game(self):
        self.controller.screen_manager.current = "level_screen"

    def back_to_menu(self):
        self.controller.screen_manager.current = "main_menu_screen"
