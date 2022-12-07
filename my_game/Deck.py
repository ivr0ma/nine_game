from random import shuffle
from Card import Card

class Deck:
    def __init__(self, cards_count):
        if cards_count == 52:
            a = 2
        else:
            a = 6

        self.cards = []
        for i in range(a, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def pop_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

    def show(self):
        cnt = 1
        for card in self.cards:
            print(cnt, card)
            cnt += 1