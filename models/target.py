from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class TargetWidget(Widget):
    def __init__(self, targets, **kwargs):
        super().__init__(**kwargs)
        self.targets = targets
        self.widget_name = "target"
        
        with self.canvas.before:
            Color(self.targets["color"])
            Rectangle(pos=self.pos, size=self.size)
