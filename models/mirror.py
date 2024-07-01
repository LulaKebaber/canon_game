from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image


class MirrorWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.widget_name = "mirror"
        
        self.image = Image(source='assets/mirror.png', size=(50, 50), pos=(100, 100))
        self.add_widget(self.image)