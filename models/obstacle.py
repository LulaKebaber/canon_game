from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class ObstacleWidget(Widget):
    def __init__(self, obstacle_info, pos, **kwargs):
        super().__init__(**kwargs)
        self.widget_name = "obstacle"
        self.obstacle_info = obstacle_info
        self.size_hint = (None, None)
        self.size = obstacle_info.get("size", [50, 50])
        self.color = obstacle_info.get("color", [0, 1, 1, 1])
        self.pos = pos

        self.update_graphics()

    def update_graphics(self):
        with self.canvas.before:
            Color(*self.color)
            self.rect = Rectangle(pos=self.pos, size=self.size)