# views/weapon_selection_screen.py
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from controllers.game_controller import GameController

Builder.load_file('views/weapon_selection_screen.kv')


class WeaponSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = kwargs.get('controller')

    def start_game(self):
        self.controller.start_game('level1', self.ids.bullets_slider.value, self.ids.bombshells_slider.value, self.ids.lasers_slider.value)
