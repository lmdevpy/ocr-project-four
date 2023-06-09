from chess.views.player_view import PlayerView


class PlayerController:

    @classmethod
    def list(cls, store, route_params=None):
        # Display the list of players and get the user choice with the player id
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
        data = PlayerView.create_player()
        store.create_player(data)
        return "list_player", None

    @classmethod
    def edit(cls, store, route_params):

        player = store.search_player(route_params)
        data = PlayerView.edit_player(player)
        player.update(data)
        store.update_json_data_file()

        return "list_player", None

    @classmethod
    def view(cls, store, route_params):

        # import pdb;pdb.set_trace()
        player = store.search_player(route_params)

        choice = PlayerView.detail_player(player)
        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "l":
            return "list_player", None
