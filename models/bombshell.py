# bombshell.py
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.graphics import Ellipse, Color
from kivy.animation import Animation
from canon_constants import BOMBSHELL_SIZE, BOMBSHELL_COLOR, FPS, INITIAL_POS, GRAVITY, SCREEN_WIDTH, SCREEN_HEIGHT


class BombShell(Widget):
    """Initializes the bombshell widget properties."""
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

        """Updates the graphics of the bullet widget.
           Uses Ellipse to draw the bullet."""
        with self.canvas:
            Color(*BOMBSHELL_COLOR)
            self.ellipse = Ellipse(pos=self.pos, size=self.size)
        self.bind(pos=self.update_graphics_pos, size=self.update_graphics_pos)
        Clock.schedule_interval(self.move, 1.0 / FPS)

    def update_graphics_pos(self, *args):
        """Updates the graphics of the bullet widget."""
        self.ellipse.pos = self.pos
        self.ellipse.size = self.size

    def move(self, dt):
        """Method to move the bullet widget."""
        if self.controller.weapon_quantities['bombshells'] > 0:
            self.velocity_y -= self.acceleration
            self.pos = Vector(*self.velocity) + self.pos

            """Checks if the bullet widget is out of bounds and resets its"""
            if self.y > SCREEN_HEIGHT or self.y < 0 or self.x > SCREEN_WIDTH or self.x < 0:
                self.reset_bombshell()
            """Checks for collisions and updates the score label.
               Collided widgets are handled by the game_controller."""
            if self.parent:
                self.collided_widgets_names = self.parent.controller.on_collision(self)
                self.handle_collision()
                self.parent.controller.update_score_label()
            """Checks if the bombshell widget is exploded and calls the explode method."""
            if self.is_exploded:
                self.explode()

    def on_touch_down(self, touch):
        """Method to handle that the bullet widget is being dragged.
           To find the start position of the bullet widget."""
        if self.collide_point(*touch.pos) and not self.is_launched:
            self.start_pos = touch.pos
            self.is_dragging = True

    def on_touch_up(self, touch):
        """Method to handle that the bullet widget is being dragged.
           To find the end position of the bullet widget and launch it.
           Also updates the bullets bullet and quantities."""
        if self.is_dragging and self.controller.weapon_quantities['bombshells'] > 0:
            self.is_dragging = False
            self.end_pos = touch.pos
            self.controller.weapon_quantities['bombshells'] -= 1
            self.move_ball()
            self.parent.controller.update_bullets_label()

    def move_ball(self):
        """Method to launch the bullet widget.
           Calculates the direction of the bullet widget and sets the velocity.
           Sets gravity as the acceleration of the bullet widget."""
        direction = Vector(*self.start_pos) - Vector(*self.end_pos)
        self.velocity = direction / 10
        self.is_launched = True
        self.acceleration = GRAVITY

    def handle_collision(self):
        """Method to handle the collision of the bullet widget with other widgets.
           If the bullet widget collides with a target, the score is updated.
           Then explosion starts.
           If the bullet widget collides with an obstacle, the bullet is reset."""
        if self.collided_widgets_names:
            for collided_widget in self.collided_widgets_names:
                if collided_widget == "target":
                    self.controller.score += 1
                    self.is_exploded = True
                elif collided_widget == "obstacle":
                    self.is_exploded = True
    
    def explode(self):
        """Method to explode the bombshell widget.
           Increases the size of the bombshell widget
           and resets it when it reaches a certain size."""
        self.velocity = Vector(0, 0)
        self.acceleration = 0
        self.size = (self.size[0] + 30, self.size[1] + 30)
        self.pos = (self.pos[0] - 15, self.pos[1] - 15)
        if self.size[0] > 200:
            self.reset_bombshell()

    def reset_bombshell(self):
        """Method to reset the laser widget to the basic properties.
           And checks if the bullets and targets are left.
           If not, the game is ended."""
        self.pos = INITIAL_POS
        self.size = BOMBSHELL_SIZE
        self.velocity = Vector(0, 0)
        self.acceleration = 0
        self.is_launched = False
        self.is_exploded = False
        if self.parent:
            self.parent.controller.check_targets_left()
            self.parent.controller.check_bullets()


