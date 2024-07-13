# controllers/game_controller.py
import json
from models.bullet import Bullet
from models.laser import Laser
from models.bombshell import BombShell


class GameController:
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

    def start_game(self, bullets, bombshells, lasers):
        self.weapon_quantities = {
            'bullets': bullets,
            'bombshells': bombshells,
            'lasers': lasers
        }
        self.weapon_quantities_initial = self.weapon_quantities.copy()
        self.screen_manager.current = "level_screen"
    
    def end_game(self):
        self.screen_manager.current = "end_game_screen"
        self.save_score(self.score)
        self.weapon_quantities = self.weapon_quantities_initial.copy()
        self.score = 0
        self.update_score_label()
        self.clear_canvas()

    def save_score(self, score):
        with open("data/records.json", "r") as file:
            records = json.load(file)
            records["records"][str(len(records["records"]) + 1)] = {
                "id": len(records["records"]) + 1,
                "score": score,
                "bullets_spent": [int(i) for i in list(self.get_weapon_bullets_spent().values())]
            }
        with open("data/records.json", "w") as file:
            json.dump(records, file)

    def get_weapon_quantities(self):
        return self.weapon_quantities
    
    def get_weapon_bullets_spent(self):
        data = {}
        data["bullets"] = self.weapon_quantities_initial["bullets"] - self.weapon_quantities["bullets"]
        data["lasers"] = self.weapon_quantities_initial["lasers"] - self.weapon_quantities["lasers"]
        data["bombshells"] = self.weapon_quantities_initial["bombshells"] - self.weapon_quantities["bombshells"]
        return data

    def update_bullets_label(self):
        bullets_label = self.level_screen.ids.bullets_label
        bullets_label.text = f"Bullets: {int(self.weapon_quantities['bullets'])}"

        lasers_label = self.level_screen.ids.lasers_label
        lasers_label.text = f"Lasers: {int(self.weapon_quantities['lasers'])}"

        bombshells_label = self.level_screen.ids.bombshells_label
        bombshells_label.text = f"Bombshells: {int(self.weapon_quantities['bombshells'])}"
    
    def check_bullets(self):
        if self.weapon_quantities['bullets'] < 1 and self.weapon_quantities['lasers'] < 1 and self.weapon_quantities['bombshells'] < 1:
            self.end_game()

    def update_score_label(self):
        score_label = self.level_screen.ids.score_label
        score_label.text = f"Score: {self.score}"

    def set_level_screen(self, level_screen):
        self.level_screen = level_screen

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
        if self.ball:
            self.level_screen.remove_widget(self.ball)
        if self.laser:
            self.level_screen.remove_widget(self.laser)
        if self.bombshell:
            self.level_screen.remove_widget(self.bombshell)

    def on_collision(self, weapon):
        collided_widgets_names = []
        for target in self.level_screen.target_layout.children:
            if hasattr(target, "widget_name"):
                if weapon and weapon.collide_widget(target):
                    collided_widgets_names.append(target.widget_name)
                    if target.widget_name == "target":
                        self.level_screen.target_layout.remove_widget(target)
        return collided_widgets_names

    def check_targets_left(self):
        targets_left = any(
            hasattr(child, 'widget_name') and child.widget_name == 'target'
            for child in self.level_screen.target_layout.children
        )
        if not targets_left:
            self.end_game()
    
    def clear_canvas(self):
        for child in self.level_screen.target_layout.children:
            if hasattr(child, 'widget_name') and (child.widget_name == 'target' or child.widget_name == 'obstacle' or child.widget_name == 'mirror'):
                self.level_screen.target_layout.remove_widget(child)
