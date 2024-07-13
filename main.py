# main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from views.main_menu import MainMenu
from views.game_screen import GameScreen
from views.select_level import SelectLevelScreen
from views.end_game_screen import EndGameScreen
from views.ranking_screen import RankingScreen
from views.weapon_selection_screen import WeaponSelectionScreen
from views.help_screen import HelpScreen
from controllers.game_controller import GameController
from controllers.ranking_controller import RankingController
from views.levels.level import Level
from kivy.config import Config
from canon_constants import SCREEN_HEIGHT, SCREEN_WIDTH
from kivy.lang import Builder

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', SCREEN_WIDTH)
Config.set('graphics', 'height', SCREEN_HEIGHT)
Builder.load_file('views/game_screen.kv')
Builder.load_file('views/levels/levels.kv')


class GameApp(App):
    def build(self):
        screen_manager = ScreenManager()

        game_controller = GameController(screen_manager=screen_manager)
        ranking_controller = RankingController(screen_manager=screen_manager)

        main_menu = MainMenu(name='main_menu_screen')
        screen_manager.add_widget(main_menu)

        game_screen = GameScreen(name='game_screen')
        game_screen.controller = game_controller
        screen_manager.add_widget(game_screen)

        select_level_screen = SelectLevelScreen(name='select_level_screen')
        select_level_screen.controller = game_controller
        screen_manager.add_widget(select_level_screen)

        weapon_selection_screen = WeaponSelectionScreen(name='weapon_selection_screen')
        weapon_selection_screen.controller = game_controller
        screen_manager.add_widget(weapon_selection_screen)

        level = Level(name='level_screen', controller=game_controller)
        screen_manager.add_widget(level)

        end_game_screen = EndGameScreen(name='end_game_screen', controller=game_controller)
        screen_manager.add_widget(end_game_screen)

        ranking_screen = RankingScreen(name='ranking_screen', controller=ranking_controller)
        screen_manager.add_widget(ranking_screen)

        help_screen = HelpScreen(name='help_screen')
        screen_manager.add_widget(help_screen)

        screen_manager.current = 'main_menu_screen'

        return screen_manager


if __name__ == '__main__':
    GameApp().run()
