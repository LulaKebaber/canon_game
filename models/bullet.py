# bullet.py
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.graphics import Ellipse, Color


class Bullet(Widget):
    widget_name = "bullet"
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    start_pos = ()
    end_pos = ()
    is_dragging = False
    is_launched = False
    acceleration = 0

    def __init__(self, controller=None, **kwargs):
        super(Bullet, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (50, 50)
        self.pos = (200, 200)
        self.controller = controller

        with self.canvas:
            Color(1, 1, 1)
            self.ellipse = Ellipse(pos=self.pos, size=self.size)
        self.bind(pos=self.update_graphics_pos, size=self.update_graphics_pos)
        Clock.schedule_interval(self.move, 1.0 / 60.0)

    def update_graphics_pos(self, *args):
        self.ellipse.pos = self.pos
        self.ellipse.size = self.size

    def move(self, dt):
        self.velocity_y -= self.acceleration
        self.pos = Vector(*self.velocity) + self.pos

        if self.y > 700 or self.y < 0 or self.x > 1000 or self.x < 0 or self.velocity_x == 0 and self.velocity_y == 0:
            self.reset_ball()
        if self.parent:
            self.parent.controller.on_collision_bullet()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and not self.is_launched:
            self.start_pos = touch.pos
            self.is_dragging = True

    def on_touch_move(self, touch):
        if self.is_dragging:
            self.end_pos = touch.pos

    def on_touch_up(self, touch):
        if self.is_dragging:
            self.is_dragging = False
            self.controller.weapon_quantities['bullets'] -= 1
            self.move_ball()
            self.parent.controller.update_bullets_label()

    def move_ball(self):
        direction = Vector(*self.end_pos) - Vector(*self.start_pos)
        self.velocity = direction * -0.1
        self.is_launched = True
        self.acceleration = 0.2

    def reset_ball(self):
        self.pos = (200, 200)
        self.velocity = Vector(0, 0)
        self.acceleration = 0
        self.is_launched = False

