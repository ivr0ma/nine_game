from Card import Card

class Board:
    def __init__(self, cards_count):
        if cards_count == 52:
            self.first = 2
        else:
            self.first = 6

        self.spades = [Card() for i in range(self.first, 15)]
        self.hearts = [Card() for i in range(self.first, 15)]
        self.diamonds = [Card() for i in range(self.first, 15)]
        self.clubs = [Card() for i in range(self.first, 15)]
        self.count = cards_count

    def push_card(self, card):
        if card.suits[card.suit] == "spades":
            self.spades[card.value-self.first] = card
            self.count -= 1
            return card.value
        if card.suits[card.suit] == "hearts":
            self.hearts[card.value-self.first] = card
            self.count -= 1
            return card.value
        if card.suits[card.suit] == "diamonds":
            self.diamonds[card.value-self.first] = card
            self.count -= 1
            return card.value
        if card.suits[card.suit] == "clubs":
            self.clubs[card.value-self.first] = card
            self.count -= 1
            return card.value
        return 0

    def show(self):
        print(self.spades)
        print(self.hearts)
        print(self.diamonds)
        print(self.clubs)

    def is_full(self):
        return self.count == 0