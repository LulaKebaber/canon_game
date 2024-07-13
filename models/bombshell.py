# bombshell.py
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.graphics import Ellipse, Color
from kivy.animation import Animation
from canon_constants import BOMBSHELL_SIZE, BOMBSHELL_COLOR, FPS, INITIAL_POS, GRAVITY, SCREEN_WIDTH, SCREEN_HEIGHT


class BombShell(Widget):
    widget_name = "bombshell"
    velocity_x, velocity_y = NumericProperty(0), NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    start_pos, end_pos = (), ()
    is_dragging, is_launched, is_exploded = False, False, False
    acceleration = 0

    def __init__(self, controller=None, **kwargs):
        super(BombShell, self).__init__(**kwargs)
        self.controller = controller
        self.collided_widgets_names = None
        self.size_hint = (None, None)
        self.size = BOMBSHELL_SIZE
        self.pos = INITIAL_POS

        with self.canvas:
            Color(*BOMBSHELL_COLOR)
            self.ellipse = Ellipse(pos=self.pos, size=self.size)
        self.bind(pos=self.update_graphics_pos, size=self.update_graphics_pos)
        Clock.schedule_interval(self.move, 1.0 / FPS)

    def update_graphics_pos(self, *args):
        self.ellipse.pos = self.pos
        self.ellipse.size = self.size

    def move(self, dt):
        self.velocity_y -= self.acceleration
        self.pos = Vector(*self.velocity) + self.pos

        if self.y > SCREEN_HEIGHT or self.y < 0 or self.x > SCREEN_WIDTH or self.x < 0:
            self.reset_bombshell()
        if self.parent:
            self.collided_widgets_names = self.parent.controller.on_collision_bombshell()
            self.handle_collision()
        if self.is_exploded:
            self.explode()

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
            self.controller.weapon_quantities['bombshells'] -= 1
            self.move_ball()
            self.parent.controller.update_bullets_label()

    def move_ball(self):
        direction = Vector(*self.start_pos) - Vector(*self.end_pos)
        self.velocity = direction / 10
        self.is_launched = True
        self.acceleration = GRAVITY

    def handle_collision(self):
        if self.collided_widgets_names:
            for collided_widget in self.collided_widgets_names:
                if collided_widget == "target":
                    self.controller.score += 1
                    self.is_exploded = True
                elif collided_widget == "obstacle":
                    self.is_exploded = True
    
    def explode(self):
        self.velocity = Vector(0, 0)
        self.acceleration = 0
        self.size = (self.size[0] + 30, self.size[1] + 30)
        self.pos = (self.pos[0] - 15, self.pos[1] - 15)
        if self.size[0] > 200:
            self.reset_bombshell()

    def reset_bombshell(self, *args):
        self.pos = INITIAL_POS
        self.size = BOMBSHELL_SIZE
        self.velocity = Vector(0, 0)
        self.acceleration = 0
        self.is_launched = False
        self.is_exploded = False


