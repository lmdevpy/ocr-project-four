from chess.views.home_view import HomeView


class HomePageController:

    @classmethod
    def dispatch(cls, store, input=None):
        # Display the home page and get the user choice
        choice = HomeView.home()
        store.initialize_json_data()  # Initialize the JSON data if needed
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
