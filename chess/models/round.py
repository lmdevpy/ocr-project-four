from datetime import datetime


class Round:
    def __init__(self, name) -> None:
        self.name = name
        self.round_number = None
        self.start_date = None
        self.end_date = None
        self.list_games = []

    def start_round(self):
        self.start_date = datetime.now().strftime("%d/%m/%Y %H:%M")

    def end_round(self):
        self.end_date = datetime.now().strftime("%d/%m/%Y %H:%M")

    def has_played_together(self, game):
        for other_game in self.list_games:
            if other_game == game:
                return True
        return False

