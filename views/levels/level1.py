# views/levels/level1.py
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from .pongball import PongBall
from kivy.graphics import Color, Rectangle

Builder.load_file('views/levels/level1.kv')


class Level1(Screen):
    grid_layout = ObjectProperty(None)

    def on_enter(self):
        self.create_targets()

    def create_targets(self):
        positions = [(100, 100), (200, 200), (300, 300)]

        for pos in positions:
            target = Widget(size_hint=(None, None), size=(30, 30))
            target.pos = pos
            with target.canvas.before:
                Color(0, 1, 0, 1)
                Rectangle(pos=target.pos, size=target.size)
            self.grid_layout.add_widget(target)

        ball = PongBall()
        ball.pos = (150, 150)
        self.add_widget(ball)
