from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('views/ranking_screen.kv')

class RankingScreen(Screen):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.controller.set_level_screen(self)

    def add_record(self, record):
        self.controller.add_record(record)

    def on_enter(self):
        self.controller.get_records()
