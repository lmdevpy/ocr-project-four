from chess.views.player_view import PlayerView


class PlayerController:

    @classmethod
    def list(cls, store, route_params=None):
        choice, player_id = PlayerView.display_list(store.players)

        if choice == "1":
            return "view_player", player_id
        elif choice == "2":
            return "edit_player", player_id
        elif choice == "3":
            return "new_player", None
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            raise Exception("invalid choice")

    @classmethod
    def create(cls, store, route_params=None):
        # call the view that will return us a dict with the new player info
        data = PlayerView.create_player()
        store.create_player(data)
        return "list_player", None

    @classmethod
    def edit(cls, store, route_params):

        player = store.search_player(route_params)
        # call the view that will return us a dict with the new player info
        data = PlayerView.edit_player(player)
        player.update(data)
        store.update_json_data_file()

        return "list_player", None

    @classmethod
    def view(cls, store, route_params):
        """
        Display one single player, the route_params correspond to the player ID
        we want to display
        """

        # import pdb;pdb.set_trace()
        player = store.search_player(route_params)

        choice = PlayerView.detail_player(player)
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "l":
            return "list_player", None