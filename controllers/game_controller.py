# controllers/game_controller.py
from kivy.uix.screenmanager import ScreenManager
from models.bullet import Bullet
from models.laser import Laser
from models.bombshell import BombShell

class GameController:
    def __init__(self, screen_manager: ScreenManager):
        self.screen_manager = screen_manager
        self.weapon_quantities = {}
        self.ball = None
        self.laser = None
        self.bombshell = None
        self.level_screen = None

    def start_game(self, level, bullets, bombshells, lasers):
        self.weapon_quantities = {
            'bullets': bullets,
            'bombshells': bombshells,
            'lasers': lasers
        }
        self.screen_manager.current = level

    def get_weapon_quantities(self):
        return self.weapon_quantities

    def set_level_screen(self, level_screen):
        self.level_screen = level_screen

    def choose_ball(self):
        if self.level_screen:
            self.clear_bullet_widgets()
            self.ball = Bullet(self)
            self.level_screen.add_widget(self.ball)
    
    def choose_laser(self):
        if self.level_screen:
            self.clear_bullet_widgets()
            self.laser = Laser(self)
            self.level_screen.add_widget(self.laser)
    
    def choose_bombshell(self):
        if self.level_screen:
            self.clear_bullet_widgets()
            self.bombshell = BombShell(self)
            self.level_screen.add_widget(self.bombshell)

    def clear_bullet_widgets(self):
        if self.level_screen:
            if self.ball:
                self.level_screen.remove_widget(self.ball)
            if self.laser:
                self.level_screen.remove_widget(self.laser)
            if self.bombshell:
                self.level_screen.remove_widget(self.bombshell)

    def on_collision(self, weapon, reset_method):
        for target in self.level_screen.target_layout.children:
            if hasattr(target, "widget_name"):
                if weapon and weapon.collide_widget(target):
                    if target.widget_name == "target":
                        self.level_screen.target_layout.remove_widget(target)
                        reset_method()
                        break
                    elif target.widget_name == "mirror" and hasattr(weapon, 'velocity_y'):
                        weapon.velocity_y *= -1
                        break

    def on_collision_bullet(self):
        self.on_collision(self.ball, self.ball.reset_ball)

    def on_collision_laser(self):
        self.on_collision(self.laser, self.laser.reset_laser)

    def on_collision_bombshell(self):
        def bombshell_reset():
            self.bombshell.animate_explosion()
        self.on_collision(self.bombshell, bombshell_reset)
