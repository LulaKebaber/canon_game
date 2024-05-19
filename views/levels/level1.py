# views/levels/level1.py
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from models.bullet import Bullet
from models.laser import Laser
from models.bombshell import BombShell
from .level_parser import LevelParser

Builder.load_file('views/levels/level1.kv')


class Level1(Screen):
    parser = LevelParser("level1")

    def __init__(self, controller=None, **kw):
        super().__init__(**kw)
        self.ball = None
        self.laser = None
        self.bombshell = None
        self.data = None
        self.weapon_quantities = None
        self.controller = controller

    def on_enter(self):
        self.data = self.parser.parse_json()
        self.weapon_quantities = self.controller.get_weapon_quantities()
        self.create_targets()
        self.create_ball()
        self.update_bullets_label()

    def create_targets(self):
        level = self.parser.parse_level()
        targets = self.parser.parse_targets()

        for pos in level["positions"]:
            target = Widget(size_hint=(None, None), size=targets["size"])
            target.pos = pos
            with target.canvas.before:
                Color(targets["color"])
                Rectangle(pos=target.pos, size=target.size)
            self.target_layout.add_widget(target)

    def update_bullets_label(self):
        bullets_label = self.ids.bullets_label
        bullets_label.text = f"Bullets: {int(self.weapon_quantities['bullets'])}"

        lasers_label = self.ids.lasers_label
        lasers_label.text = f"Lasers: {int(self.weapon_quantities['lasers'])}"

        bombshells_label = self.ids.bombshells_label
        bombshells_label.text = f"Bombshells: {int(self.weapon_quantities['bombshells'])}"

    def create_ball(self):
        self.ball = Bullet(self.controller)
        self.laser = Laser(self.controller)
        self.bombshell = BombShell(self.controller)
        self.add_widget(self.ball)
        self.add_widget(self.laser)
        self.add_widget(self.bombshell)

    def on_collision(self):
        for target in self.target_layout.children[:]:
            if self.ball.collide_widget(target):
                self.target_layout.remove_widget(target)
                self.ball.reset_ball()
                break

            if self.laser.collide_widget(target):
                self.target_layout.remove_widget(target)
                self.laser.reset_laser()
                break

            if self.bombshell.collide_widget(target):
                self.bombshell.animate_explosion()
                self.target_layout.remove_widget(target)
                break