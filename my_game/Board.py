from Card import Card

class Board:
    def __init__(self, cards_count):
        if cards_count == 52:
            self.first = 2
        else:
            self.first = 6

        self.spades = ['_' for i in range(self.first, 15)]
        self.hearts = ['_' for i in range(self.first, 15)]
        self.diamonds = ['_' for i in range(self.first, 15)]
        self.clubs = ['_' for i in range(self.first, 15)]
        self.count = cards_count

    def push_card(self, card):
        if card.suits[card.suit] == "spades":
            self.spades[card.value-self.first] = str(card.values[card.value]) + " s"
            self.count -= 1
            return card.value
        if card.suits[card.suit] == "hearts":
            self.hearts[card.value-self.first] = str(card.values[card.value]) + " h"
            self.count -= 1
            return card.value
        if card.suits[card.suit] == "diamonds":
            self.diamonds[card.value-self.first] = str(card.values[card.value]) + " d"
            self.count -= 1
            return card.value
        if card.suits[card.suit] == "clubs":
            self.clubs[card.value-self.first] = str(card.values[card.value]) + " c"
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