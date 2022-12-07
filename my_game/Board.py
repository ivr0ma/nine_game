from Card import Card

class Board:
    def __init__(self):
        self.spades = ['_' for i in range(2,15)]
        self.hearts = ['_' for i in range(2,15)]
        self.diamonds = ['_' for i in range(2,15)]
        self.clubs = ['_' for i in range(2,15)]

    def push_card(self, card):
        if card.suits[card.suit] == "spades":
            self.spades[card.value-2] = str(card.values[card.value]) + " s"
            return card.value
        if card.suits[card.suit] == "hearts":
            self.hearts[card.value-2] = str(card.values[card.value]) + " h"
            return card.value
        if card.suits[card.suit] == "diamonds":
            self.diamonds[card.value-2] = str(card.values[card.value]) + " d"
            return card.value
        if card.suits[card.suit] == "clubs":
            self.clubs[card.value-2] = str(card.values[card.value]) + " c"
            return card.value
        return 0

    def show(self):
        print(self.spades)
        print(self.hearts)
        print(self.diamonds)
        print(self.clubs)