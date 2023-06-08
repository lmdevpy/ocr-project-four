from texttable import Texttable


class TournamentView:

    @classmethod
    def display_list(cls, tournaments):
        table = Texttable()
        table.header(["Id", "Name", "Location", "Start Date", "End Date", "Number Of Rounds", "Number of players"])
        for tournament in tournaments:
            table.add_row([tournament.id, tournament.name, tournament.location, tournament.start_date,
                           tournament.end_date, tournament.number_of_rounds,
                           tournament.number_of_players])

        print(table.draw())

        print("1. View Tournament Details")
        print("2. Start/Continue Tournament")
        print("3. Create New Tournament")
        print("Q. Exit")
        print("H. Homepage")

        choice = input("Choice:")
        extra_info = None

        if choice in ("1", "2"):
            extra_info = int(input("Enter Tournament Id:"))

        return choice, extra_info

    @classmethod
    def detail_tournament(cls, tournament):
        print(f"\n\tId: {tournament.id}")
        print(f"\tName: {tournament.name}")
        print(f"\tLocation: {tournament.location}")
        print(f"\tNumber of players: {tournament.number_of_players}")
        print(f"\tNumber of rounds: {tournament.number_of_rounds}")
        if tournament.current_round_number:
            print(f"\tCurrent round: {tournament.current_round_number}")
        if tournament.start_date:
            print(f"\tStart date: {tournament.start_date}")
        else:
            print("\tStart date: Not started yet")
        if tournament.end_date:
            print(f"\tEnd date: {tournament.end_date}")
        if tournament.list_of_players:
            print(f"\tPlayers list: ", end="")
            new_players_list = sorted(tournament.list_of_players, key=lambda p: p.name)
            for player in new_players_list:
                print(f"{player.name}", end=", ")
        if tournament.final_ranking:
            print(f"\n\tFinal ranking: ", end="")
            for i, player in enumerate(tournament.final_ranking, start=1):
                print(f"{i}: (name:{player.name} score: {player.scores[tournament.id]}),", end=" ")
        if tournament.rounds_list:
            print("\n")
            for round in tournament.rounds_list:
                print(f"\t{round.name} :")
                for i, game in enumerate(round.games_list, start=1):
                    if not game.isFinished:
                        print(f"\t\tmatch {i} : {game.player_1.name} contre {game.player_2.name}")
                    else:
                        if game.score_player_1 > game.score_player_2:
                            print(f"\t\tmatch {i} : {game.player_1.name} contre {game.player_2.name} -> Winner :"
                                  f" {game.player_1.name}")
                        elif game.score_player_2 > game.score_player_1:
                            print(f"\t\tmatch {i} : {game.player_1.name} contre {game.player_2.name} -> Winner :"
                                  f" {game.player_2.name}")
                        else:
                            print(f"\t\tmatch {i} : {game.player_1.name} contre {game.player_2.name} -> Winner : DRAW")

        print("\nQ. Exit")
        print("L. Return To Tournaments list")
        print("H. Homepage")
        return input("Choice:")

    @classmethod
    def create_tournament(cls):
        return {
            "id": input("Enter an ID: "),
            "name": input("Enter a name: "),
            "location": input("Enter a location: "),
            "number_of_rounds": input("Enter a number of rounds: "),
            "number_of_players": input("Enter a number of players: "),
            "description": input("Enter a description: ")
        }

    @classmethod
    def start_tournament(cls, tournament):
        if tournament.start_date:
            print(f"are you sure to continue '{tournament.name}'")
            print("\npress y for Yes")
            print("press n for No")
            return input("Choice: ")
        else:
            print(f"are you sure to start the tournament '{tournament.name}'")
            print("\nY. Yes")
            print("N. No")
            return input("Choice:")

    @classmethod
    def add_players(cls, players, tournament):

        table = Texttable()
        table.header(["Id", "Name", "age", "email"])
        for player in players:
            table.add_row([player.id, player.name, player.age, player.email])
        print(table.draw())

        list_players = []

        for i in range(1, int(tournament.number_of_players)+1):
            player_id = int(input(f'Enter ID player {i}: '))
            list_players.append(player_id)

        return list_players

    @classmethod
    def set_rounds(cls, tournament):
        print(f"\n\tTournament name: {tournament.name}")
        print(f"\tLocation: {tournament.location}")
        print(f"\tNumber of players: {tournament.number_of_players}")
        print(f"\tNumber of rounds: {tournament.number_of_rounds}")
        if not tournament.current_round_number:
            print(f"\n\tCurrent round: Tournament has not started yet")
            print("\n1. Start the first round")
            print("2. return to home page")
            return input("\nChoice:")
        else:
            print(f"\n\tCurrent round: {tournament.current_round_number}\n")
            for round in tournament.rounds_list:
                if round.round_number == tournament.current_round_number:
                    if not round.end_date:
                        for i, game in enumerate(round.games_list, start=1):
                            if not game.isFinished:
                                print(f"match {i} : {game.player_1.name} contre {game.player_2.name}")
                            else:
                                if game.score_player_1 > game.score_player_2:
                                    print(f"match {i} : {game.player_1.name} contre {game.player_2.name} -> Winner :"
                                          f" {game.player_1.name}")
                                elif game.score_player_2 > game.score_player_1:
                                    print(f"match {i} : {game.player_1.name} contre {game.player_2.name} -> Winner :"
                                          f" {game.player_2.name}")
                                else:
                                    print(f"match {i} : {game.player_1.name} contre {game.player_2.name} -> Winner : DRAW")
                        print("\n")
                        for i, game in enumerate(round.games_list, start=1):
                            if not game.isFinished:
                                print(f"{i}: Entrer le resultat du match {i}")
                        print("Q. Exit")
                        return input("Choice: ")
                    else:
                        if not tournament.current_round_number == int(tournament.number_of_rounds):
                            print(f"Lancer le prochain round ?")
                            print("press y for yes")
                            print("press n for No and quit")
                            return input("Choice: ")
                        else:
                            print("TOURNAMENT FINISHED !")
                            input("Press Enter to continue")


    @classmethod
    def set_games_result(cls, game):
        print(f'1. {game.player_1.name} win')
        print(f'2. {game.player_2.name} win')
        print(f'3. draw')
        return input("Choice: ")

    @classmethod
    def error_page(cls, message):
        print(message)
        input("Press Enter to continue")
