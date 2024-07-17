# projectile.py
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.graphics import Ellipse, Color
from canon_constants import FPS, INITIAL_POS, GRAVITY, SCREEN_WIDTH, SCREEN_HEIGHT

class Projectile(Widget):
    """Initializes the projectile widget properties."""
    widget_name = "projectile"
    velocity_x, velocity_y = NumericProperty(0), NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    start_pos, end_pos = (), ()
    is_dragging, is_launched = False, False

    def __init__(self, controller=None, size=None, color=None, **kwargs):
        super(Projectile, self).__init__(**kwargs)
        self.controller = controller
        self.collided_widgets = None
        self.size_hint = (None, None)
        self.size = size
        self.pos = INITIAL_POS
        self.acceleration = 0
        
        """Draws the projectile widget on the screen."""
        with self.canvas:
            Color(*color)
            self.ellipse = Ellipse(pos=self.pos, size=self.size)
        self.bind(pos=self.update_graphics_pos, size=self.update_graphics_pos)
        Clock.schedule_interval(self.move, 1.0 / FPS)

    """"""
    def update_graphics_pos(self, *args):
        """Updates the graphics of the projectile widget."""
        self.ellipse.pos = self.pos
        self.ellipse.size = self.size

    def move(self, dt):
        """Method to move the projectile widget."""
        if self.controller and self.controller.weapon_quantities[self.widget_name] > 0:
            self.velocity_y -= self.acceleration
            self.pos = Vector(*self.velocity) + self.pos

            if self.y > SCREEN_HEIGHT or self.y < 0 or self.x > SCREEN_WIDTH or self.x < 0:
                self.reset_projectile()
            
            if self.parent:
                self.collided_widgets = self.parent.controller.on_collision(self)
                self.handle_collision()
                self.parent.controller.update_score_label()

    def on_touch_down(self, touch):
        """Method to handle that the projectile widget is being dragged."""
        if self.collide_point(*touch.pos) and not self.is_launched:
            self.start_pos = touch.pos
            self.is_dragging = True

    def on_touch_up(self, touch):
        """Method to handle that the projectile widget is being dragged."""
        if self.is_dragging and self.controller and self.controller.weapon_quantities[self.widget_name] > 0:
            self.end_pos = touch.pos
            self.is_dragging = False
            self.controller.weapon_quantities[self.widget_name] -= 1
            self.parent.controller.update_bullets_label()
            self.launch()

    def launch(self):
        """Method to launch the projectile widget."""
        direction = Vector(*self.start_pos) - Vector(*self.end_pos)
        self.velocity = direction / 10
        self.is_launched = True
        self.acceleration = GRAVITY

    def reset_projectile(self):
        """Method to reset the projectile widget to the basic properties."""
        self.pos = INITIAL_POS
        self.velocity = Vector(0, 0)
        self.acceleration = 0
        self.is_launched = False
        if self.parent:
            self.parent.controller.check_targets_left()
            self.parent.controller.check_bullets()
            