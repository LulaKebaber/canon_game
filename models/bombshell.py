# bombshell.py
from .projectile import Projectile
from canon_constants import BOMBSHELL_SIZE, BOMBSHELL_COLOR
from kivy.vector import Vector


class BombShell(Projectile):
    widget_name = "bombshells"
    is_exploded = False

    def __init__(self, controller=None, **kwargs):
        super(BombShell, self).__init__(
            controller=controller, size=BOMBSHELL_SIZE, color=BOMBSHELL_COLOR, **kwargs)

    def handle_collision(self):
        if self.collided_widgets:
            for collided_widget in self.collided_widgets:
                if collided_widget == "target":
                    self.controller.score += 1
                    self.is_exploded = True
                elif collided_widget == "obstacle":
                    self.is_exploded = True
    
    def move(self, dt):
        super(BombShell, self).move(dt)
        if self.is_exploded:
            self.explode()

    def explode(self):
        self.velocity = Vector(0, 0)
        self.acceleration = 0
        self.size = (self.size[0] + 30, self.size[1] + 30)
        self.pos = (self.pos[0] - 15, self.pos[1] - 15)
        if self.size[0] > 200:
            self.reset_projectile()

    def reset_projectile(self):
        super(BombShell, self).reset_projectile()
        self.size = BOMBSHELL_SIZE
        self.is_exploded = False
