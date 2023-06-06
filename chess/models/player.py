class Player:
    def __init__(self, id, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email
        self.id = id
        self.score = 0

    def update(self, data):
        if data["name"]:
            self.name = data["name"]
        if data["age"]:
            self.age = data["age"]
        if data["email"]:
            self.email = data["email"]
