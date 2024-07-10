# views/end_game_screen.py
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('views/end_game_screen.kv')

class EndGameScreen(Screen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
    
    def on_restart_game(self):
        self.controller.screen_manager.current = "level1"

    def on_main_menu(self):
        self.controller.screen_manager.current = "main_menu"
