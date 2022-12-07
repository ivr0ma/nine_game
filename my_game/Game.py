from Player import Player
from Deck import Deck
from Board import Board
from Card import Card

class Game:
    def __init__(self, cards_count):
        self.deck = Deck(cards_count)
        self.board = Board(cards_count)
        self.first_number = self.get_first(cards_count)
        self.pl = Player("you")
        self.ai = Player("AI")
        self.available_cards = [Card(9, 0), Card(9, 1), Card(9, 2), Card(9, 3)]

        for i in range(18):
            self.pl.cards.append(self.deck.pop_card())
        for i in range(18):
            self.ai.cards.append(self.deck.pop_card())

        self.pl.sort()
        self.ai.sort()

        self.pl.show()
        self.ai.show()

        self.board.show()

    def get_first(self, count):
        if count == 52:
            return 2
        else:
            return 6

    def is_available(self, card):
        if card in self.available_cards:
            return True
        else:
            return False

    def get_number(self):
        count = len(self.ai.cards)

        for i in range(count):
            if self.is_available(self.ai.cards[i]):
                return i

        return -1

    def in_board(self, card):
        if card.suit == 0:
            return card in self.board.spades
        if card.suit == 1:
            return card in self.board.hearts
        if card.suit == 2:
            return card in self.board.diamonds
        if card.suit == 3:
            return card in self.board.clubs

    def add_availabel_cards(self, card):
        if card.value > self.first_number:
            new_card = Card(card.value - 1, card.suit)
            if not self.in_board(new_card):
                self.available_cards.append(new_card)
            if card.value < 14:
                new_card = Card(card.value + 1, card.suit)
                if not self.in_board(new_card):
                    self.available_cards.append(new_card)
        else:
            new_card = Card(card.value + 1, card.suit)
            if not self.in_board(new_card):
                self.available_cards.append(new_card)

    def ai_move(self):
        self.ai.show()
        ai_number = self.get_number()
        if (ai_number != -1):
            card = self.ai.pop_card(ai_number)
            self.board.push_card(card)
            print(f"ai choose number {ai_number}")
            self.add_availabel_cards(card)
            self.available_cards.remove(card)
        else:
            print("ai: skipping a move")

    def player_move(self):
        while True:
            self.pl.show()
            number = int(input("choice number (or -1) "))

            if number == -1:
                print("player: skipping a move")
                return

            if number > (len(self.pl.cards)-1):
                print("choose another card")
                continue

            if not self.is_available(self.pl.cards[number]):
                print("choose another card")
                continue
            else:
                break

        card = self.pl.pop_card(number)
        self.board.push_card(card)
        self.add_availabel_cards(card)
        self.available_cards.remove(card)

    def play_game(self):
        print("beginning War!")
        active_player = "ai"

        while not self.board.is_full():
            print(f"availabel cards: ", self.available_cards)

            if active_player == "ai":
                self.ai_move()
                active_player = "you"
            else:
                self.player_move()
                active_player = "ai"

            self.board.show()
            print()

            if (self.pl.cards == []):
                print("You win!")
                return 0

            if (self.ai.cards == []):
                print("AI win!")
                return 0

        print("end.")