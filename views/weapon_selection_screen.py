# views/weapon_selection_screen.py
from kivy.uix.screenmanager import Screen

class WeaponSelectionScreen(Screen):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        
    def start_game(self):
        """Starts the game with current slider values."""
        self.controller.start_game(self.ids.bullets_slider.value, self.ids.bombshells_slider.value, self.ids.lasers_slider.value)

    def update_bullets_label(self, value):
        """Updates bullets label with the given slider value."""
        self.ids.bullets_value.text = str(int(value))

    def update_lasers_label(self, value):
        """Updates lasers label with the given slider value."""
        self.ids.lasers_value.text = str(int(value))

    def update_bombshells_label(self, value):
        """Updates bombshells label with the given slider value."""
        self.ids.bombshells_value.text = str(int(value))
