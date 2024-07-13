from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class TargetWidget(Widget):
    def __init__(self, target_info, pos, **kwargs):
        super().__init__(**kwargs)
        self.widget_name = "target"
        self.target_info = target_info
        self.size_hint = (None, None)
        self.size = target_info.get("size", [70, 70])
        self.color = target_info.get("color", [1, 1, 1, 1])
        self.pos = pos

        self.update_graphics()

    def update_graphics(self):
        with self.canvas.before:
            Color(*self.color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
    