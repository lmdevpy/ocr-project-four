from datetime import datetime
from chess.models.game import Game


class Round:
    def __init__(self, name) -> None:
        self.name = name
        self.round_number = None
        self.start_date = None
        self.end_date = None
        self.games_list = []

    def to_dict(self):
        return {
            "name": self.name,
            "round_number": self.round_number,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "games_list": [game.to_dict() for game in self.games_list]
        }

    @classmethod
    def from_dict(cls, data):
        games_data = data.pop("games_list", [])
        round = cls.__new__(cls)
        for key, value in data.items():
            setattr(round, key, value)
        round.games_list = [Game.from_dict(game_data) for game_data in games_data]
        return round

    def start_round(self):
        self.start_date = datetime.now().strftime("%d/%m/%Y %H:%M")

    def end_round(self):
        self.end_date = datetime.now().strftime("%d/%m/%Y %H:%M")

    def has_played_together(self, game):
        for other_game in self.games_list:
            if other_game == game:
                return True
        return False

