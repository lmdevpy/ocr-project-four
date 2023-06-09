from chess.controllers.home_controller import HomePageController
from chess.models.store import Store
from chess.controllers.player_controller import PlayerController
from chess.controllers.tournament_controller import TournamentController
import subprocess as sp


# The Application class represents the main application that handles routing and controller dispatching.
class Application:
    # The routes dictionary maps route names to their corresponding controller methods.
    routes = {
        "homepage": HomePageController.dispatch,
        "new_tournament": TournamentController.create,
        "list_tournament": TournamentController.list,
        "view_tournament": TournamentController.details,
        "start_tournament": TournamentController.start,
        "add_players_tournament": TournamentController.add_players,
        "set_rounds_tournament": TournamentController.set_rounds,
        "set_games_result": TournamentController.set_games_result,
        "list_player": PlayerController.list,
        "edit_player": PlayerController.edit,
        "new_player": PlayerController.create,
        "view_player": PlayerController.view,
        "error_page": TournamentController.error_page
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False # to control the application loop.
        self.route_params = None# Parameters for the current route.
        self.store = Store()

    def run(self):
        while not self.exit:
            # Clear the shell output
            sp.call('cls', shell=True)
            # Get the controller method that should handle our current route
            controller_method = self.routes[self.route]

            # Call the controller method, passing the store and the route's parameters.
            # The controller should return the next route and parameters.
            next_route, next_params = controller_method(
                self.store, self.route_params
            )

            # set the next route and parameterss
            self.route = next_route
            self.route_params = next_params

            # if the controller return "quit" then we end the application
            if next_route == "quit":
                self.exit = True
