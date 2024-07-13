from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image


class MirrorWidget(Widget):
    def __init__(self, pos, **kwargs):
        super().__init__(**kwargs)
        self.widget_name = "mirror"
        self.size_hint = (None, None)
        self.pos = pos
        
        self.image = Image(source='assets/mirror.png', size=self.size, pos=self.pos)
        self.add_widget(self.image)