# views/levels/level1.py
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
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

    def __init__(self, controller, **kw):
        super().__init__(**kw)
        self.weapon_quantities = None
        self.controller = controller
        self.controller.set_level_screen(self)

    def on_enter(self):
        self.weapon_quantities = self.controller.get_weapon_quantities()
        self.create_targets()
        self.controller.update_bullets_label()
        self.controller.update_score_label()

    def create_targets(self):
        level = self.parser.parse_level()
        targets = self.parser.parse_targets()

        for pos in level["positions"]:
            target = TargetWidget(pos=pos, targets=targets)
            self.target_layout.add_widget(target)
        
        mirror = MirrorWidget(pos=(400, 20), size=(100, 50))
        self.target_layout.add_widget(mirror)

    def choose_ball(self):
        self.controller.choose_ball()
    
    def choose_laser(self):
        self.controller.choose_laser()

    def choose_bombshell(self):
        self.controller.choose_bombshell()
