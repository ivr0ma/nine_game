from Player import Player
from Deck import Deck
from Board import Board

class Game:
    def __init__(self, cards_count):
        self.deck = Deck(cards_count)
        self.board = Board(cards_count)
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

        self.board.show()

    def wins(self, winner):
        print(f'{winner} wins this round')

    def draw(self, p1n, p1c, p2n, p2c):
        print(f'{p1n} drew {p1c} {p2n} drew {p2c}')

    def play_game(self):
        print("beginning War!")

        while not self.board.is_full():
            self.board.push_card(self.ai.pop_card())
            self.board.push_card(self.pl.pop_card())

            self.board.show()
            print()


    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"