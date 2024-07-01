# views/levels/level1.py
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from models.bullet import Bullet
from models.laser import Laser
from models.bombshell import BombShell
from models.target import TargetWidget
from models.mirror import MirrorWidget
from .level_parser import LevelParser
from kivy.config import Config

Builder.load_file('views/levels/level1.kv')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')

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
        self.update_bullets_label()

    def create_targets(self):
        level = self.parser.parse_level()
        targets = self.parser.parse_targets()

        for pos in level["positions"]:
            target = TargetWidget(size=targets["size"], pos=pos, targets=targets)
            self.target_layout.add_widget(target)
        
        mirror = MirrorWidget(pos=(100, 100), size=(50, 50))
        self.target_layout.add_widget(mirror)

    def update_bullets_label(self):
        bullets_label = self.ids.bullets_label
        bullets_label.text = f"Bullets: {int(self.weapon_quantities['bullets'])}"

        lasers_label = self.ids.lasers_label
        lasers_label.text = f"Lasers: {int(self.weapon_quantities['lasers'])}"

        bombshells_label = self.ids.bombshells_label
        bombshells_label.text = f"Bombshells: {int(self.weapon_quantities['bombshells'])}"

    def on_collision(self):
        for target in self.target_layout.children[:]:
            if self.ball:
                if self.ball.collide_widget(target) and target.widget_name == "target":
                    self.target_layout.remove_widget(target)
                    self.ball.reset_ball()
                    break
            if self.laser:
                if self.laser.collide_widget(target):
                    if target.widget_name == "target":
                        self.target_layout.remove_widget(target)
                        self.laser.reset_laser()
                        break
                    elif target.widget_name == "mirror":
                        self.laser.velocity_y *= -1
                        break
            if self.bombshell:
                if self.bombshell.collide_widget(target) and target.widget_name == "target":
                    self.bombshell.animate_explosion()
                    self.target_layout.remove_widget(target)
                    break
    
    def choose_ball(self):
        if self.ball:
            self.remove_widget(self.ball)
        if self.laser:
            self.remove_widget(self.laser)
        if self.bombshell:
            self.remove_widget(self.bombshell)
        self.ball = Bullet(self.controller)
        self.add_widget(self.ball)

    def choose_laser(self):
        if self.laser:
            self.remove_widget(self.laser)
        if self.ball:
            self.remove_widget(self.ball)
        if self.bombshell:
            self.remove_widget(self.bombshell)
        self.laser = Laser(self.controller)
        self.add_widget(self.laser)

    def choose_bombshell(self):
        if self.bombshell:
            self.remove_widget(self.bombshell)
        if self.ball:
            self.remove_widget(self.ball)
        if self.laser:
            self.remove_widget(self.laser)
        self.bombshell = BombShell(self.controller)
        self.add_widget(self.bombshell)
    