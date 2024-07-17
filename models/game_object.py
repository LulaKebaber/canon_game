# game_object.py
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class GameObject(Widget):
    def __init__(self, info, pos, **kwargs):
        """Initializes the game object properties."""
        super().__init__(**kwargs)
        self.widget_name = info.get("name", "game_object")
        self.size_hint = (None, None)
        self.size = info.get("size")
        self.color = info.get("color")
        self.pos = pos

        self.update_graphics()

    def update_graphics(self):
        """Updates the graphics of the game object."""
        with self.canvas.before:
            Color(*self.color)
            self.rect = Rectangle(pos=self.pos, size=self.size)