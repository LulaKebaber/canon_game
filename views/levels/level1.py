from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('views/levels/level1.kv')

from kivy.graphics import Color, Rectangle


class Level1(Screen):
    grid_layout = ObjectProperty(None)

    def on_enter(self):
        self.create_targets()

    def create_targets(self):
        targets_layout = self.grid_layout

        # Список с координатами для каждого квадрата
        positions = [(100, 100), (200, 200), (300, 300)]

        for pos in positions:
            target = Widget(size_hint=(None, None), size=(30, 30))
            target.pos = pos  # Установка координат для квадрата
            with target.canvas.before:
                Color(0, 1, 0, 1)  # Зеленый цвет (RGBA: (0, 1, 0, 1))
                Rectangle(pos=target.pos, size=target.size)
            targets_layout.add_widget(target)
