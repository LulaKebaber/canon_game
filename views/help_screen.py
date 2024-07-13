from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
import webbrowser

class HelpScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def back_to_menu(self):
        """Changes the screen to the main menu screen."""
        self.manager.current = 'main_menu_screen'
    
    def open_github_repo(self):
        """Opens the GitHub repository in the web browser."""
        webbrowser.open('https://github.com/LulaKebaber/cannongamedemo')

