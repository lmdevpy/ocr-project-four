from chess.views.home_view import HomeView


class HomePageController:

    @classmethod
    def dispatch(cls, store=None, input=None):
        choice = HomeView.home()
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
