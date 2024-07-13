import json
from kivy.uix.label import Label

class RankingController:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.records = []

    def set_level_screen(self, level_screen):
        """Set the level screen to the ranking controller to update the table."""
        self.level_screen = level_screen

    def add_record(self, record):
        """Add a record to the records list and update the table."""
        self.records.append(record)
        self.update_table()

    def update_table(self):
        """Update the table with the records."""
        record_table = self.level_screen.ids.record_table
        record_table.clear_widgets()
        
        """Add the headers of the table."""
        i = 1
        while i < len(self.records) + 1:
            record = self.records[str(i)]
            bullets = record['bullets_spent'][0]
            lasers = record['bullets_spent'][1]
            bombshells = record['bullets_spent'][2]

            """Add the records to the table."""
            record_table.add_widget(Label(text=str(i), font_size='18sp', size_hint_y=None, height=40))
            record_table.add_widget(Label(text=str(record['score']), font_size='18sp', size_hint_y=None, height=40))
            record_table.add_widget(Label(text=str(bullets), font_size='18sp', size_hint_y=None, height=40))
            record_table.add_widget(Label(text=str(lasers), font_size='18sp', size_hint_y=None, height=40))
            record_table.add_widget(Label(text=str(bombshells), font_size='18sp', size_hint_y=None, height=40))
            i += 1
            
    def get_records(self):
        """Get the records from the records.json file."""
        with open("data/records.json", 'r') as file:
            data = json.load(file)
            self.records = data.get("records", [])
            self.update_table()
