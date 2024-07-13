# select_level.py
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class SelectLevelScreen(Screen):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller

    def on_button_release(self, instance):
        self.controller.selected_level = f"level{instance.text.split()[-1]}"
        self.manager.current = "weapon_selection_screen"
