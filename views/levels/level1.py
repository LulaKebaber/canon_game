# views/levels/level1.py
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from models.bullet import Bullet
from .level_parser import LevelParser

Builder.load_file('views/levels/level1.kv')


class Level1(Screen):
    parser = LevelParser("level1")

    def __init__(self, **kw):
        super().__init__(**kw)
        self.ball = None
        self.data = None

    def on_enter(self):
        self.data = self.parser.parse_json()
        self.create_targets()
        self.create_ball()

    def create_targets(self):
        level = self.parser.parse_level()
        targets = self.parser.parse_targets()

        for pos in level["positions"]:
            target = Widget(size_hint=(None, None), size=targets["size"])
            target.pos = pos
            print(target.pos)
            with target.canvas.before:
                Color(targets["color"])
                Rectangle(pos=target.pos, size=target.size)
            self.target_layout.add_widget(target)

    def create_ball(self):
        self.ball = Bullet()
        self.add_widget(self.ball)

    def on_collision(self):
        for target in self.target_layout.children[:]:
            if self.ball.collide_widget(target):
                self.target_layout.remove_widget(target)
                self.ball.reset_ball()
                break
