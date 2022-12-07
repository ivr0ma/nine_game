from random import shuffle
from Card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(6, 15):
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