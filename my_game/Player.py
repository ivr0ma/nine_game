class Player:
    def __init__(self, name):
        self.wins = 0
        self.cards = []
        self.name = name

    def show(self):
        print(f"{self.name}: {self.cards}")

    def sort(self):
        self.cards = sorted(self.cards)