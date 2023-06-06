import random
from datetime import datetime
from chess.models.round import Round
from chess.models.game import Game
from itertools import combinations


class Tournament:
    def __init__(self, id, name, location, number_of_rounds, number_of_players, description) -> None:
        self.id = id
        self.name = name
        self.location = location
        self.start_date = None
        self.end_date = None
        self.number_of_rounds = number_of_rounds
        self.number_of_players = number_of_players
        self.current_round_number = None
        self.rounds_list = []
        self.list_of_players = []
        self.description = description

    def start_tournament(self):
        self.start_date = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.current_round_number = 1

    def end_tournament(self):
        self.end_date = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.current_round_number = "Tournament finished"

    def set_first_round_matches(self):
        randomized_player_list = random.sample(self.list_of_players, len(self.list_of_players))
        round_1 = Round("round 1")
        for i in range(0, len(randomized_player_list), 2):
            player_1 = randomized_player_list[i]
            player_2 = randomized_player_list[i + 1]
            game = Game(player_1, player_2)
            round_1.list_games.append(game)
        round_1.start_round()
        round_1.round_number = self.current_round_number
        self.rounds_list.append(round_1)

    def set_other_rounds(self):
        self.sort_players_by_point()
        for i in range(2, self.number_of_rounds + 1):
            new_round = Round(f"round {i}")
            if not self.is_round_present(new_round):
                pairs = list(combinations(self.list_of_players, 2))
                used_players = []
                for player_1, player_2 in pairs:
                    game = Game(player_1, player_2)
                    for round in self.rounds_list:
                        if not round.has_played_together(game):
                            if player_1 not in used_players and player_2 not in used_players:
                                used_players.append(player_1)
                                used_players.append(player_2)
                                new_round.list_games.append(Game(player_1, player_2))
                new_round.start_round()
                new_round.round_number = self.current_round_number
                self.rounds_list.append(new_round)
                break

    def sort_players_by_point(self):
        self.list_of_players = sorted(self.list_of_players, key=lambda player: player.score, reverse=True)

    def is_round_present(self, new_round):
        for round in self.rounds_list:
            if round.name == new_round.name:
                return True
        return False
