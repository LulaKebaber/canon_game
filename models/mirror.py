from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Rectangle, Color

class MirrorWidget(Widget):
    def __init__(self, pos, **kwargs):
        """Initializes the mirror widget properties."""
        super().__init__(**kwargs)
        self.widget_name = "mirror"
        self.size_hint = (None, None)
        self.pos = pos
        
        self.image = Image(source='assets/mirror.png')
        self.size = self.image.texture_size

        self.update_graphics()
    
    def update_graphics(self):
        """Updates the graphics of the mirror widget."""
        with self.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(texture=self.image.texture, pos=self.pos, size=self.size)
