from chess.models.player import Player


class Game:
    def __init__(self, player_1, player_2) -> None:
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = None
        self.score_player_2 = None
        self.isFinished = False

    def to_dict(self):
        return {
            "player_1": self.player_1.to_dict(),
            "player_2": self.player_2.to_dict(),
            "score_player_1": self.score_player_1,
            "score_player_2": self.score_player_2,
            "isFinished": self.isFinished
        }

    @classmethod
    def from_dict(cls, data):
        player_1_data = data.pop("player_1", {})  # Extraire les données du joueur 1
        player_2_data = data.pop("player_2", {})  # Extraire les données du joueur 2
        game = cls.__new__(cls)
        for key, value in data.items():
            setattr(game, key, value)
        game.player_1 = Player.from_dict(player_1_data) if player_1_data else None
        game.player_2 = Player.from_dict(player_2_data) if player_2_data else None
        return game

    def __eq__(self, other):
        if isinstance(other, Game):
            if self.player_1 == other.player_1 and self.player_2 == other.player_2 or \
                    self.player_1 == other.player_2 and self.player_2 == other.player_1:
                return True
        return False

    def set_player1_wins(self, tournament_id):
        self.score_player_1 = 1
        self.score_player_2 = 0
        self.player_1.scores[tournament_id] += 1

    def set_player2_wins(self, tournament_id):
        self.score_player_1 = 0
        self.score_player_2 = 1
        self.player_2.scores[tournament_id] += 1

    def set_draw(self, tournament_id):
        self.score_player_1 = 0.5
        self.score_player_2 = 0.5
        self.player_1.scores[tournament_id] += 0.5
        self.player_2.scores[tournament_id] += 0.5

    def finished(self):
        self.isFinished = True
