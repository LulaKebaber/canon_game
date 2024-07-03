from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class TargetWidget(Widget):
    def __init__(self, targets, **kwargs):
        super().__init__(**kwargs)
        self.widget_name = "target"
        self.targets = targets
        self.size_hint = (None, None)
        self.size = targets["size"]

        with self.canvas.before:
            Color(self.targets["color"])
            Rectangle(pos=self.pos, size=self.size)
