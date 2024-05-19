from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.graphics import Ellipse, Color
from kivy.animation import Animation
from kivy.properties import ListProperty


class Bombshell(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    start_pos = ()
    end_pos = ()
    is_dragging = False
    is_launched = False
    is_exploded = False
    acceleration = 0
    explosion_radius = 50

    def __init__(self, controller=None, **kwargs):
        super(Bombshell, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (30, 30)
        self.controller = controller

        with self.canvas:
            Color([1, 0, 0, 1])
            self.ellipse = Ellipse(pos=self.pos, size=self.size)
        self.bind(pos=self.update_graphics_pos, size=self.update_graphics_pos)

    def update_graphics_pos(self, *args):
        self.ellipse.pos = self.pos
        self.ellipse.size = self.size

    def move(self):
        self.velocity_y -= self.acceleration
        self.pos = Vector(*self.velocity) + self.pos

        if self.y > 1400 or self.y < 0 or self.x > 2000 or self.x < 0 or self.velocity_x == 0 and self.velocity_y == 0:
            self.reset_bombshell()
        if self.parent:
            self.parent.on_collision()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and not self.is_launched:
            self.start_pos = self.pos
            self.is_dragging = True

    def on_touch_move(self, touch):
        if self.is_dragging:
            self.end_pos = touch.pos

    def on_touch_up(self, touch):
        if self.is_dragging:
            self.is_dragging = False
            self.launch_bomb()

    def launch_bomb(self):
        direction = Vector(*self.end_pos) - Vector(*self.start_pos)
        self.velocity = direction * -0.1
        self.is_launched = True
        self.acceleration = 0.2
        # Clock.schedule_once(self.explode, 0.5)

    def explode(self, *args):
        targets = self.parent.level.children[:]
        bomb_center = Vector(*self.center)
        for target in targets:
            target_center = Vector(*target.center)
            distance = bomb_center.distance(target_center)
            if distance <= self.explosion_radius:
                self.parent.level.remove_widget(target)
                self.is_exploded = True
                Clock.schedule_once(self.animate_explosion)

    def animate_explosion(self, *args):
        if self.is_exploded:
            explosion_animation = Animation(size=(100, 100), duration=0.5)
            explosion_animation += Animation(color=(1, 1, 0, 1), duration=0.5)
            explosion_animation.bind(on_complete=self.reset_bombshell)
            explosion_animation.start(self)

    def reset_bombshell(self, instance=None, value=None):
        self.pos = (300, 300)
        self.velocity = Vector(0, 0)
        self.acceleration = 0
        self.is_launched = False
        self.is_exploded = False
