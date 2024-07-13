# views/levels/level.py
from kivy.uix.screenmanager import Screen
from models.target import TargetWidget
from models.obstacle import ObstacleWidget
from models.mirror import MirrorWidget
from controllers.level_parser import LevelParser


class Level(Screen):
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.weapon_quantities = None
        self.controller = controller
        self.controller.set_level_screen(self)
        self.parser = LevelParser()

    def on_enter(self):
        self.weapon_quantities = self.controller.get_weapon_quantities()
        self.initialize_level()
        self.controller.update_bullets_label()
        self.controller.update_score_label()

    def initialize_level(self):
        if self.controller.selected_level:
            self.parser.level = self.controller.selected_level
        self.level_info = self.parser.parse_level_info()
        self.create_targets()
        self.create_obstacles()
        self.create_mirrors()
    
    def create_targets(self):
        target_info = self.parser.parse_targets_properties()

        for pos in self.level_info["target_positions"]:
            target = TargetWidget(pos=pos, target_info=target_info)
            self.target_layout.add_widget(target)

    def create_obstacles(self):
        obstacle_info = self.parser.parse_obstacle_properties()

        for pos in self.level_info["obstacle_positions"]:
            obstacle = ObstacleWidget(pos=pos, obstacle_info=obstacle_info)
            self.target_layout.add_widget(obstacle)

    def create_mirrors(self):
        for pos in self.level_info["mirror_positions"]:
            mirror = MirrorWidget(pos=pos)
            self.target_layout.add_widget(mirror)

    def choose_ball(self):
        self.controller.choose_ball()
    
    def choose_laser(self):
        self.controller.choose_laser()

    def choose_bombshell(self):
        self.controller.choose_bombshell()
