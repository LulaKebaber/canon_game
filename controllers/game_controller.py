# controllers/game_controller.py
import json
from models.bullet import Bullet
from models.laser import Laser
from models.bombshell import BombShell


class GameController:
    """GameController class is responsible for managing the game logic."""
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.selected_level = None
        self.weapon_quantities = {}
        self.weapon_quantities_initial = {}
        self.score = 0
        self.ball = None
        self.laser = None
        self.bombshell = None
        self.level_screen = None

    def set_level_screen(self, level_screen):
        """Set the level screen to the game controller to update the data."""
        self.level_screen = level_screen

    def start_game(self, bullets, bombshells, lasers):
        """Start the game with the given quantities of bullets, bombshells, and lasers.
           And checks if chosen quantities are valid."""
        self.weapon_quantities = {
            'bullets': bullets,
            'bombshells': bombshells,
            'lasers': lasers
        }
        self.weapon_quantities_initial = self.weapon_quantities.copy()
        self.screen_manager.current = "level_screen"
        self.check_bullets()
    
    def end_game(self):
        """Method to end the game and save the score.
           Updates and resets the score, weapon quantities, and the screen.
           Clears the canvas from all the widgets."""
        self.screen_manager.current = "end_game_screen"
        self.save_score(self.score)
        self.weapon_quantities = self.weapon_quantities_initial.copy()
        self.score = 0
        self.update_score_label()
        self.clear_canvas()

    def save_score(self, score):
        """Save the score and bullets spent to the records.json file.
           And then sorts the records."""
        bullets_spent = [int(i) for i in list(self.get_weapon_bullets_spent().values())]
        self.level_screen.parser.save_score(score, bullets_spent)
        self.level_screen.parser.sort_records()

    def get_weapon_quantities(self):
        return self.weapon_quantities
    
    def get_weapon_bullets_spent(self):
        """Returns the bullets spent for each weapon type."""
        data = {}
        data["bullets"] = self.weapon_quantities_initial["bullets"] - self.weapon_quantities["bullets"]
        data["lasers"] = self.weapon_quantities_initial["lasers"] - self.weapon_quantities["lasers"]
        data["bombshells"] = self.weapon_quantities_initial["bombshells"] - self.weapon_quantities["bombshells"]
        return data

    def update_bullets_label(self):
        """Update the bullets labels with the current weapon quantities."""
        bullets_label = self.level_screen.ids.bullets_label
        bullets_label.text = f"Bullets: {int(self.weapon_quantities['bullets'])}"

        lasers_label = self.level_screen.ids.lasers_label
        lasers_label.text = f"Lasers: {int(self.weapon_quantities['lasers'])}"

        bombshells_label = self.level_screen.ids.bombshells_label
        bombshells_label.text = f"Bombshells: {int(self.weapon_quantities['bombshells'])}"
    
    def update_score_label(self):
        """Update the score label with the current score."""
        score_label = self.level_screen.ids.score_label
        score_label.text = f"Score: {self.score}"    

    """These three methods are responsible for choosing the weapon type.
       It clears the bullet widgets from the screen
       and adds the chosen weapon to the screen."""
    def choose_ball(self):
        self.clear_bullet_widgets()
        self.ball = Bullet(self)
        self.level_screen.add_widget(self.ball)
    
    def choose_laser(self):
        self.clear_bullet_widgets()
        self.laser = Laser(self)
        self.level_screen.add_widget(self.laser)
    
    def choose_bombshell(self):
        self.clear_bullet_widgets()
        self.bombshell = BombShell(self)
        self.level_screen.add_widget(self.bombshell)

    def clear_bullet_widgets(self):
        """Clears the bullet widgets from the screen."""
        if self.ball:
            self.level_screen.remove_widget(self.ball)
        if self.laser:
            self.level_screen.remove_widget(self.laser)
        if self.bombshell:
            self.level_screen.remove_widget(self.bombshell)

    def on_collision(self, weapon):
        """Method to check the collision of the weapon with the target, mirror, and obstacle.
           Returns the collided widgets names.
           And then in their models handle the collision."""
        collided_widgets_names = []
        for target in self.level_screen.target_layout.children:
            if hasattr(target, "widget_name"):
                if weapon and weapon.collide_widget(target):
                    collided_widgets_names.append(target.widget_name)
                    if target.widget_name == "target":
                        self.level_screen.target_layout.remove_widget(target)
        return collided_widgets_names

    def check_targets_left(self):
        """Method to check if there are any targets left on the screen.
           If not, ends the game."""
        targets_left = any(
            hasattr(child, 'widget_name') and child.widget_name == 'target'
            for child in self.level_screen.target_layout.children
        )
        if not targets_left:
            self.end_game()
    
    def clear_canvas(self):
        """Clears the canvas from all the widgets after the game ends."""
        for child in self.level_screen.target_layout.children:
            if hasattr(child, 'widget_name') and (child.widget_name == 'target' or child.widget_name == 'obstacle' or child.widget_name == 'mirror'):
                self.level_screen.target_layout.remove_widget(child)

    def check_bullets(self):
        """Method to check if there are any bullets left.
           If not, ends the game."""
        if self.weapon_quantities['bullets'] < 1 and self.weapon_quantities['lasers'] < 1 and self.weapon_quantities['bombshells'] < 1:
            self.end_game()