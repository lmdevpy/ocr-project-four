class Player:
    def __init__(self, id, name, age, email) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.scores = {}

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "scores": self.scores
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(data['id'], data['name'], data['age'], data['email'])
        player.scores = data.get('scores', {})
        scores = {int(key): value for key, value in player.scores.items()}
        player.scores = scores
        return player

    def update(self, data):
        if data["name"]:
            self.name = data["name"]
        if data["age"]:
            self.age = data["age"]
        if data["email"]:
            self.email = data["email"]
