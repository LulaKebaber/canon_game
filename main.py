# main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from views.main_menu import MainMenu
from views.game_screen import GameScreen
from views.end_game_screen import EndGameScreen
from views.ranking_screen import RankingScreen
from views.weapon_selection_screen import WeaponSelectionScreen
from controllers.game_controller import GameController
from controllers.ranking_controller import RankingController
from views.levels.level1 import Level1
from kivy.config import Config
from canon_constants import SCREEN_HEIGHT, SCREEN_WIDTH
from kivy.lang import Builder


Config.set('graphics', 'width', SCREEN_WIDTH)
Config.set('graphics', 'height', SCREEN_HEIGHT)
Builder.load_file('views/game_screen.kv')
Builder.load_file('views/levels/level1.kv')

class GameApp(App):
    def build(self):
        # Создание экземпляра менеджера экранов
        screen_manager = ScreenManager()

        # Создание экземпляра GameController
        game_controller = GameController(screen_manager=screen_manager)
        ranking_controller = RankingController(screen_manager=screen_manager)

        # Добавление экрана главного меню и передача контроллера
        main_menu = MainMenu(name='main_menu')
        main_menu.controller = game_controller
        screen_manager.add_widget(main_menu)

        # Добавление экрана игры и передача контроллера
        game_screen = GameScreen(name='game_screen')
        game_screen.controller = game_controller
        screen_manager.add_widget(game_screen)

        # Добавление экрана выбора оружия и передача контроллера
        weapon_selection_screen = WeaponSelectionScreen(name='weapon_selection_screen')
        weapon_selection_screen.controller = game_controller
        screen_manager.add_widget(weapon_selection_screen)

        # добавление первого уровня
        level1 = Level1(name='level1', controller=game_controller)
        screen_manager.add_widget(level1)

        end_game_screen = EndGameScreen(name='end_game_screen', controller=game_controller)
        screen_manager.add_widget(end_game_screen)
        # end_game_screen.controller = game_controller

        ranking_screen = RankingScreen(name='ranking_screen', controller=ranking_controller)
        screen_manager.add_widget(ranking_screen)

        # Устанавливаем главный экран как текущий
        screen_manager.current = 'main_menu'

        return screen_manager


if __name__ == '__main__':
    GameApp().run()
