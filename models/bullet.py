# bullet.py
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.graphics import Ellipse, Color
from canon_constants import BULLET_SIZE, BULLET_COLOR, FPS, INITIAL_POS, GRAVITY, SCREEN_WIDTH, SCREEN_HEIGHT


class Bullet(Widget):
    widget_name = "bullet"
    velocity_x, velocity_y = NumericProperty(0), NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    start_pos, end_pos = (), ()
    is_dragging, is_launched = False, False

    def __init__(self, controller=None, **kwargs):
        super(Bullet, self).__init__(**kwargs)
        self.controller = controller
        self.collided_widgets = None
        self.size_hint = (None, None)
        self.size = BULLET_SIZE
        self.pos = INITIAL_POS
        self.acceleration = 0
        
        with self.canvas:
            Color(*BULLET_COLOR)
            self.ellipse = Ellipse(pos=self.pos, size=self.size)
        self.bind(pos=self.update_graphics_pos, size=self.update_graphics_pos)
        Clock.schedule_interval(self.move, 1.0 / FPS)

    def update_graphics_pos(self, *args):
        self.ellipse.pos = self.pos
        self.ellipse.size = self.size

    def move(self, dt):
        if self.controller.weapon_quantities['bullets'] > 0:
            self.velocity_y -= self.acceleration
            self.pos = Vector(*self.velocity) + self.pos

            if self.y > SCREEN_HEIGHT or self.y < 0 or self.x > SCREEN_WIDTH or self.x < 0 or self.velocity_x == 0 and self.velocity_y == 0:
                self.reset_bullet()
            if self.parent:
                self.collided_widgets = self.parent.controller.on_collision(self)
                self.handle_collision()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and not self.is_launched:
            self.start_pos = touch.pos
            self.is_dragging = True

    def on_touch_up(self, touch):
        if self.is_dragging and self.controller.weapon_quantities['bullets'] > 0:
            self.end_pos = touch.pos
            self.is_dragging = False
            self.controller.weapon_quantities['bullets'] -= 1
            self.parent.controller.update_bullets_label()
            self.move_ball()

    def move_ball(self):
        direction = Vector(*self.start_pos) - Vector(*self.end_pos)
        self.velocity = direction / 10
        self.is_launched = True
        self.acceleration = GRAVITY

    def handle_collision(self):
        if self.collided_widgets:
            if self.collided_widgets[0] == "target":
                self.controller.score += 1
                self.reset_bullet()
            elif self.collided_widgets[0] == "obstacle":
                self.reset_bullet()

    def reset_bullet(self):
        self.pos = INITIAL_POS
        self.velocity = Vector(0, 0)
        self.acceleration = 0
        self.is_launched = False

