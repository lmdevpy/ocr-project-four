from texttable import Texttable


class PlayerView:

    # Method to display a list of the players
    @classmethod
    def display_list(cls, players):
        table = Texttable()
        table.header(["Id", "Name", "age", "email"])
        players_new_list = sorted(players, key=lambda player: player.name)
        for player in players_new_list:
            table.add_row([player.name, player.id, player.age, player.email])
        print(table.draw())

        print("1. View Player")
        print("2. Edit Player")
        print("3. New Player")
        print("Q. Exit")
        print("H. Homepage")

        choice = input("Choice:")
        extra_info = None

        if choice in ("1", "2"):
            extra_info = int(input("Enter Player Id:"))

        return choice, extra_info

    # Method to display the details of a player
    @classmethod
    def detail_player(cls, player):
        print(f"Id: {player.id}")
        print(f"Name: {player.name}")
        print(f"Age: {player.age}")
        print(f"Email: {player.email}")
        print(f"Scores: {player.scores}")

        print("Q. Exit")
        print("L. Return To List")
        print("H. Homepage")
        return input("Choice:")

    # Method to insert the datas of a player to create
    @classmethod
    def create_player(cls):
        return {
            "id": input("Enter an ID: "),
            "name": input("Enter a name: "),
            "age": input("Enter an age: "),
            "email": input("Enter an email: ")
        }

    # method to edit the datas of a player already created
    @classmethod
    def edit_player(cls, player):
        return {
            "name": input(f"Edit name (default: {player.name}): "),
            "age": input(f"Edit age (default: {player.age}): "),
            "email": input(f"Edit email (default: {player.email}): ")
        }
