from chess.models.player import Player
from chess.models.tournament import Tournament


class Store:

    def __init__(self):
        self.tournaments = [
            Tournament(2356, "Tournament of Belgrade", "BELGRADE/SERBIA", 4, 8,
                       "The Serbia Open is a professional tournament"),
        ]
        self.players = [
                Player(1, "Pablo", 36, "test@test.com"),
                Player(2, "Michel", 40, "test@test.com"),
                Player(3, "Moustafa", 23, "test@test.com"),
                Player(4, "sofian", 26, "test@test.com"),
                Player(5, "gregory", 56, "test@test.com"),
                Player(6, "Mathieu", 60, "test@test.com"),
                Player(7, "jean", 30, "test@test.com"),
                Player(8, "mehdi", 40, "test@test.com"),

            ]

    # save data to json file
    def save(self):
        pass

    def search_player(self, player_id):
        return next(p for p in self.players if p.id == player_id)

    def search_tournament(self, tournament_id):
        return next(t for t in self.tournaments if t.id == tournament_id)

    def create_player(self, player_data):
        player_data["id"] = int(player_data["id"])
        player = Player(**player_data)
        self.players.append(player)

    def create_tournament(self, tournament_data):
        tournament_data["id"] = int(tournament_data["id"])
        tournament = Tournament(**tournament_data)
        self.tournaments.append(tournament)
