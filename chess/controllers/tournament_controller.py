from chess.views.tournament_view import TournamentView


class TournamentController:

    @classmethod
    def list(cls, store, route_params=None):
        choice, tournament_id = TournamentView.display_list(store.tournaments)
        if tournament_id:
            tournament = store.search_tournament(tournament_id)

        if choice == "1":
            return "view_tournament", tournament_id
        elif choice == "2" and not tournament.end_date:
            return "start_tournament", tournament_id
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

        # import pdb;pdb.set_trace()
        tournament = store.search_tournament(route_params)

        # we pass the tournament to the view that will display the player info and
        # the next options
        choice = TournamentView.detail_tournament(tournament)
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "l":
            return "list_tournament", None

    @classmethod
    def start(cls, store, route_params):
        tournament = store.search_tournament(route_params)
        choice = TournamentView.start_tournament(tournament)

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
        tournament = store.search_tournament(route_params)
        players_ids = TournamentView.add_players(store.players, tournament)

        list_players = []

        try:
            for player_id in players_ids:
                player = store.search_player(player_id)
                list_players.append(player)

            tournament.list_of_players = list_players
            return "set_rounds_tournament", tournament.id
        except StopIteration:
            return "error_page", "player not found"

    @classmethod
    def set_rounds(cls, store, route_params):
        tournament = store.search_tournament(route_params)
        if not tournament.current_round_number:
            choice = TournamentView.set_rounds(tournament)
            if choice == "1":
                tournament.start_tournament()
                tournament.set_first_round_matches()
                return "set_rounds_tournament", tournament.id
            else:
                return "list_tournament", None
        else:
            for round in tournament.rounds_list:
                if round.round_number == tournament.current_round_number:
                    if not round.end_date:
                        if not all(game.isFinished for game in round.list_games):
                            choice = TournamentView.set_rounds(tournament)
                            for i, game in enumerate(round.list_games, start=1):
                                if choice == f"{i}" and not game.isFinished:
                                    return "set_games_result", {"tournament": tournament.id, "game": game}
                                if choice.lower() == 'q':
                                    return "list_tournament", None
                            if choice:
                                print("invalid choice")
                                return "set_rounds_tournament", tournament.id
                        else:
                            round.end_round()
                            choice = TournamentView.set_rounds(tournament)
                            if not tournament.current_round_number == tournament.number_of_rounds:
                                if choice.lower() == "y":
                                    tournament.current_round_number += 1
                                    tournament.set_other_rounds()
                                    return "set_rounds_tournament", tournament.id
                                else:
                                    return "list_tournament", None
                            else:
                                tournament.end_tournament()
                                tournament.sort_players_by_point()
                                return "list_tournament", None

    @classmethod
    def set_games_result(cls, store, dict):
        tournament = store.search_tournament(dict["tournament"])
        choice = TournamentView.set_games_result(dict["game"])
        if choice == "1":
            dict["game"].set_player1_wins()
        if choice == "2":
            dict["game"].set_player2_wins()
        if choice == "3":
            dict["game"].set_draw()
        dict["game"].finished()
        return "set_rounds_tournament", tournament.id

    @classmethod
    def error_page(cls, store, route_params):
        TournamentView.error_page(message=route_params)

        return "homepage", None
