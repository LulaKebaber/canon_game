# select_level.py
from kivy.uix.screenmanager import Screen


class SelectLevelScreen(Screen):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller

    def on_button_release(self, instance):
        """Sets the selected level based on the button text and switches to the next screen."""
        self.controller.selected_level = f"level{instance.text.split()[-1]}"
        self.manager.current = "weapon_selection_screen"
