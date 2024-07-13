# ranking_screen.py
from kivy.uix.screenmanager import Screen

class RankingScreen(Screen):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.controller.set_level_screen(self)

    def add_record(self, record):
        """Adds a new record to the ranking table."""
        self.controller.add_record(record)

    def on_enter(self):
        """Called when the screen is entered, retrieves records from the controller."""
        self.controller.get_records()

    def back_to_menu(self):
        """Switches the screen back to the main menu screen."""
        self.manager.current = 'main_menu_screen'
