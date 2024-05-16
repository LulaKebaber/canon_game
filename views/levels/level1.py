# views/levels/level1.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty


class Target(Widget):
    pass


class Level1(Screen):
    def on_enter(self):
        self.create_targets()

    def create_targets(self):
        targets_layout = self.ids.targets_layout
        for _ in range(3):
            target = Target()
            targets_layout.add_widget(target)