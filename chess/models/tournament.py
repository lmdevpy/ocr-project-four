import random
from datetime import datetime
from chess.models.round import Round
from chess.models.game import Game
from chess.models.player import Player
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
        self.final_ranking = []
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_rounds": self.number_of_rounds,
            "number_of_players": self.number_of_players,
            "current_round_number": self.current_round_number,
            "rounds_list": [round.to_dict() for round in self.rounds_list],
            "list_of_players": [player.to_dict() for player in self.list_of_players],
            "final_ranking": [player.to_dict() for player in self.final_ranking],
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data):
        players_data = data.pop("list_of_players", [])
        rounds_data = data.pop("rounds_list", [])
        rank_data = data.pop("final_ranking", [])
        tournament = cls.__new__(cls)
        for key, value in data.items():
            setattr(tournament, key, value)
        tournament.list_of_players = [Player.from_dict(player_data) for player_data in players_data]
        tournament.rounds_list = [Round.from_dict(round_data) for round_data in rounds_data]
        tournament.final_ranking = [Player.from_dict(rank) for rank in rank_data]
        return tournament

    def start_tournament(self):
        self.start_date = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.current_round_number = 1

    def end_tournament(self):
        self.end_date = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.current_round_number = "Tournament finished"
        self.final_ranking = sorted(self.list_of_players, key=lambda player: player.scores[self.id], reverse=True)

    def set_first_round_matches(self):
        randomized_player_list = random.sample(self.list_of_players, len(self.list_of_players))
        round_1 = Round("round 1")
        for i in range(0, len(randomized_player_list), 2):
            player_1 = randomized_player_list[i]
            player_2 = randomized_player_list[i + 1]
            game = Game(player_1, player_2)
            round_1.games_list.append(game)
        round_1.start_round()
        round_1.round_number = self.current_round_number
        self.rounds_list.append(round_1)

    def set_other_rounds(self):
        self.sort_players_by_point()
        for i in range(2, int(self.number_of_rounds) + 1):
            new_round = Round(f"round {i}")
            if not self.is_round_present(new_round):
                pairs = list(combinations(self.list_of_players, 2))
                used_players = []
                for player_1, player_2 in pairs:
                    game = Game(player_1, player_2)
                    if not any(round.has_played_together(game) for round in self.rounds_list):
                        if player_1 not in used_players and player_2 not in used_players:
                            used_players.append(player_1)
                            used_players.append(player_2)
                            new_round.games_list.append(game)
                new_round.start_round()
                new_round.round_number = self.current_round_number
                self.rounds_list.append(new_round)
                break

    def sort_players_by_point(self):
        self.list_of_players = sorted(self.list_of_players, key=lambda player: player.scores[self.id], reverse=True)

    def is_round_present(self, new_round):
        for round in self.rounds_list:
            if round.name == new_round.name:
                return True
        return False
