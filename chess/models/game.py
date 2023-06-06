class Game:
    def __init__(self, player_1, player_2) -> None:
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = None
        self.score_player_2 = None
        self.isFinished = False

    def __eq__(self, other):
        if isinstance(other, Game):
            if self.player_1 == other.player_1 and self.player_2 == other.player_2 or \
                    self.player_1 == other.player_2 and self.player_2 == other.player_1:
                return True
        return False

    def set_player1_wins(self):
        self.score_player_1 = 1
        self.score_player_2 = 0
        self.player_1.score += 1

    def set_player2_wins(self):
        self.score_player_1 = 0
        self.score_player_2 = 1
        self.player_2.score += 1

    def set_draw(self):
        self.score_player_1 = 0.5
        self.score_player_2 = 0.5
        self.player_1.score += 0.5
        self.player_2.score += 0.5

    def finished(self):
        self.isFinished = True
