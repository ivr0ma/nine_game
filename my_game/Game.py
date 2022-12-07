import pylab as pl

from Player import Player
from Deck import Deck

class Game:
    def __init__(self):
        self.deck = Deck()
        self.pl = Player("you")
        self.ai = Player("AI")

        for i in range(18):
            self.pl.cards.append(self.deck.pop_card())
        for i in range(18):
            self.ai.cards.append(self.deck.pop_card())

        self.pl.sort()
        self.ai.sort()

        self.pl.show()
        self.ai.show()

    def wins(self, winner):
        print(f'{winner} wins this round')

    def draw(self, p1n, p1c, p2n, p2c):
        print(f'{p1n} drew {p1c} {p2n} drew {p2c}')

    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any " + "key to play:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.pop_card()
            p2c = self.deck.pop_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print(f"War is over.{win} wins")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"