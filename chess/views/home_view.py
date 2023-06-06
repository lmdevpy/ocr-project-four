class HomeView:

    @classmethod
    def home(cls):
        print("Welcome\n")
        print("1. List Players")
        print("2. New Player")
        print("3. List Tournaments")
        print("4. New Tournament\n")
        print("Q. Exit")

        return input("Choice: ")
