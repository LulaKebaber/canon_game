# bullet.py
from .projectile import Projectile
from canon_constants import BULLET_SIZE, BULLET_COLOR

class Bullet(Projectile):
    widget_name = "bullets"

    def __init__(self, controller=None, **kwargs):
        super(Bullet, self).__init__(controller=controller, size=BULLET_SIZE, color=BULLET_COLOR, **kwargs)

    def handle_collision(self):
        if self.collided_widgets:
            if self.collided_widgets[0] == "target":
                self.controller.score += 1
                self.reset_projectile()
            elif self.collided_widgets[0] == "obstacle":
                self.reset_projectile()