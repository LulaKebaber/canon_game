from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.graphics import Color, Line, Ellipse
from canon_constants import LASER_SIZE, LASER_VEL, INITIAL_POS, LASER_COLOR, FPS, SCREEN_HEIGHT, SCREEN_WIDTH

class Laser(Widget):
    widget_name = "laser"
    velocity_x, velocity_y = NumericProperty(0), NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    start_pos, end_pos = (), ()
    is_dragging, is_launched = False, False
    speed = LASER_VEL

    def __init__(self, controller=None, **kwargs):
        super(Laser, self).__init__(**kwargs)
        self.controller = controller
        self.collided_widgets = None
        self.size_hint = (None, None)
        self.size = LASER_SIZE
        self.pos = INITIAL_POS
        self.path_points = []

        with self.canvas:
            Color(*LASER_COLOR)
            self.ellipse = Ellipse(pos=self.pos, size=self.size)
            Color(*LASER_COLOR)
            self.line = Line(points=[], width=LASER_SIZE[0] / 2)
        self.bind(pos=self.update_graphics_pos, size=self.update_graphics_pos)
        Clock.schedule_interval(self.move, 1.0 / FPS)

    def update_graphics_pos(self, *args):
        self.ellipse.pos = self.pos
        self.ellipse.size = self.size

    def move(self, dt):
        if self.controller.weapon_quantities['lasers'] > 0:
            self.pos = Vector(*self.velocity) + self.pos

            if self.is_launched:
                self.path_points.extend([self.center_x, self.center_y])
                self.line.points = self.path_points

            if self.y > SCREEN_HEIGHT or self.y < 0 or self.x > SCREEN_WIDTH or self.x < 0:
                self.reset_laser()

            if self.parent:
                self.collided_widgets = self.parent.controller.on_collision(self)
                self.handle_collision()
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and not self.is_launched:
            self.start_pos = touch.pos
            self.is_dragging = True

    def on_touch_move(self, touch):
        if self.is_dragging:
            self.end_pos = touch.pos

    def on_touch_up(self, touch):
        if self.is_dragging and self.controller.weapon_quantities['lasers'] > 0:
            self.is_dragging = False
            self.end_pos = touch.pos
            self.controller.weapon_quantities['lasers'] -= 1
            self.parent.controller.update_bullets_label()
            self.launch()

    def launch(self):
        direction = Vector(*self.end_pos) - Vector(*self.start_pos)
        if direction.length() == 0:
            direction = Vector(-1, 0)
        self.velocity = direction.normalize() * -self.speed
        self.is_launched = True
        self.path_points = [self.center_x, self.center_y]

    def handle_collision(self):
        if self.collided_widgets:
            for collided_widget in self.collided_widgets:
                if collided_widget == "target":
                    self.controller.score += 1
                elif collided_widget == "mirror":
                    self.velocity_y *= -1

    def reset_laser(self):
        self.pos = INITIAL_POS
        self.velocity = Vector(0, 0)
        self.is_launched = False
        self.path_points = []
        self.line.points = []
