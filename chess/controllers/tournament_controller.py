from chess.views.tournament_view import TournamentView


class TournamentController:

    @classmethod
    def list(cls, store, route_params=None):
        # Display the list of tournaments and get the user choice with the tournament id
        choice, tournament_id = TournamentView.display_list(store.tournaments)
        if choice == "1":
            return "view_tournament", tournament_id
        elif choice == "2":
            tournament = store.search_tournament(tournament_id)
            if not tournament.end_date:
                return "start_tournament", tournament_id
            else:
                print("Tournament is already finished")
                return "list_tournament", None
        elif choice == "3":
            return "new_tournament", None
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            raise Exception("invalid choice")

    @classmethod
    def create(cls, store, route_params=None):
        data = TournamentView.create_tournament()
        store.create_tournament(data)
        return "list_tournament", None

    @classmethod
    def details(cls, store, route_params):
        # Display tournament details and get the user choice for the next step
        tournament = store.search_tournament(route_params)

        choice = TournamentView.detail_tournament(tournament)
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "l":
            return "list_tournament", None

    @classmethod
    def start(cls, store, route_params):
        # Display the start tournament prompt and get the user choice
        tournament = store.search_tournament(route_params)
        choice = TournamentView.start_tournament(tournament)
        # The next route depending on the state of the tournament
        if choice.lower() == "y" and not tournament.list_of_players:
            return "add_players_tournament", tournament.id
        elif choice.lower() == "y" and tournament.list_of_players:
            return "set_rounds_tournament", tournament.id
        elif choice.lower() == "n":
            return "list_tournament", None
        else:
            print("invalid choice")

        return "list_tournament", None

    @classmethod
    def add_players(cls, store, route_params):
        # Add the selected players to the tournament and initialize their scores
        tournament = store.search_tournament(route_params)
        players_ids = TournamentView.add_players(store.players, tournament)

        list_players = []

        try:
            for player_id in players_ids:
                player = store.search_player(player_id)
                player.scores[tournament.id] = 0
                list_players.append(player)

            tournament.list_of_players = list_players
            store.update_json_data_file()
            return "set_rounds_tournament", tournament.id
        except StopIteration:
            return "error_page", "player not found"

    @classmethod
    def set_rounds(cls, store, route_params):
        tournament = store.search_tournament(route_params)
        # If the current round number is not set, prompt the user to set the first round
        if not tournament.current_round_number:
            choice = TournamentView.set_rounds(tournament)
            if choice == "1":
                tournament.start_tournament()
                tournament.set_first_round_games()
                store.update_json_data_file()
                return "set_rounds_tournament", tournament.id
            else:
                return "list_tournament", None
        else:
            for round in tournament.rounds_list:
                if round.round_number == tournament.current_round_number:
                    if not round.end_date:
                        if not all(game.isFinished for game in round.games_list):
                            # If the round is not finished and there is games left, prompt the user to set games result
                            choice = TournamentView.set_rounds(tournament)
                            for i, game in enumerate(round.games_list, start=1):
                                if choice == f"{i}" and not game.isFinished:
                                    # User chose a game to set the result
                                    return "set_games_result", {"tournament": tournament.id, "game": game}
                                if choice.lower() == 'q':
                                    return "list_tournament", None
                            if choice:
                                print("invalid choice")
                                return "set_rounds_tournament", tournament.id
                        else:
                            # If all games in the round are finished, end the round
                            round.end_round()
                            store.update_json_data_file()
                            choice = TournamentView.set_rounds(tournament)
                            if not tournament.current_round_number == tournament.number_of_rounds:
                                if choice.lower() == "y":
                                    # User chose to proceed to the next round
                                    tournament.current_round_number += 1
                                    tournament.set_other_rounds()
                                    store.update_json_data_file()
                                    return "set_rounds_tournament", tournament.id
                                else:
                                    return "list_tournament", None
                            else:
                                # If it's the final round and all games are finished then we end the tournament
                                tournament.end_tournament()
                                store.update_json_data_file()
                                return "view_tournament", tournament.id

    @classmethod
    def set_games_result(cls, store, dict):
        # Display the game result prompt and get the result with the user choice
        tournament = store.search_tournament(dict["tournament"])
        choice = TournamentView.set_games_result(dict["game"])
        if choice == "1":
            dict["game"].set_player1_wins(tournament.id)
        if choice == "2":
            dict["game"].set_player2_wins(tournament.id)
        if choice == "3":
            dict["game"].set_draw(tournament.id)
        dict["game"].finished()
        store.update_json_data_file()
        return "set_rounds_tournament", tournament.id

    @classmethod
    def error_page(cls, store, route_params):
        TournamentView.error_page(message=route_params)

        return "homepage", None
