from chess.models.player import Player
from chess.models.tournament import Tournament
import os
import json


class Store:

    def __init__(self):
        self.tournaments = []
        self.players = []
        self.initialized = False

    def initialize_json_data(self):
        file_path = "data_tournaments.json"
        if os.path.isfile(file_path):
            if not self.initialized:
                self.read_json_file()
                self.initialized = True
            else:
                pass
        else:
            data = {
                "tournaments": [],
                "players": [],
            }
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
            self.tournaments = data["tournaments"]
            self.players = data["players"]
            self.initialized = True

    def update_json_data_file(self):
        list_of_tournaments_dict = [tournament.to_dict() for tournament in self.tournaments]
        list_of_players_dict = [player.to_dict() for player in self.players]
        data = {'tournaments': list_of_tournaments_dict, 'players': list_of_players_dict}
        with open("data_tournaments.json", "w") as file:
            json.dump(data, file, indent=4)

    def read_json_file(self):

        with open('data_tournaments.json', 'r') as file:
            data = json.load(file)
        tournaments_data = data['tournaments']
        players_data = data['players']
        self.tournaments = [Tournament.from_dict(tournament_data) for tournament_data in tournaments_data]
        self.players = [Player.from_dict(player_data) for player_data in players_data]

    def search_player(self, player_id):
        return next(p for p in self.players if p.id == player_id)

    def search_tournament(self, tournament_id):
        return next(t for t in self.tournaments if t.id == tournament_id)

    def create_player(self, player_data):
        player_data["id"] = int(player_data["id"])
        player = Player(**player_data)
        self.players.append(player)
        self.update_json_data_file()

    def create_tournament(self, tournament_data):
        tournament_data["id"] = int(tournament_data["id"])
        tournament_data["number_of_rounds"] = int(tournament_data["number_of_rounds"])
        tournament = Tournament(**tournament_data)
        self.tournaments.append(tournament)
        self.update_json_data_file()
