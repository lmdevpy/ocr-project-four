from chess.views.home_view import HomeView


class HomePageController:

    @classmethod
    def dispatch(cls, store, input=None):
        choice = HomeView.home()
        store.initialize_json_data()
        if choice.lower() == "q":
            next = "quit"
        elif choice == "1":
            next = "list_player"
        elif choice == "2":
            next = "new_player"
        elif choice == "3":
            next = "list_tournament"
        elif choice == "4":
            next = "new_tournament"
        return next, None
