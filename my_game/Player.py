class Player:
    def __init__(self, name):
        self.wins = 0
        self.cards = []
        self.name = name

    def show(self):
        print(f"{self.name}: ", end="")
        cnt = 0
        for card in self.cards:
            print(f"{cnt}: ({card}) ", end="")
            cnt += 1
        print()

    def sort(self):
        self.cards = sorted(self.cards)

    def pop_card(self, number):
        if self.cards == []:
            return None
        else:
            return self.cards.pop(number)