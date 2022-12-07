class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    values = [None, None, None, None,
              None, None, "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.suit < c2.suit:
            return True
        if self.suit == c2.suit:
            if self.value < c2.value:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.suit > c2.suit:
            return True
        if self.suit == c2.suit:
            if self.value > c2.value:
                return True
            else:
                return False
        return False

    def __le__(self, c2):
        if self.suit <= c2.suit:
            return True
        if self.suit == c2.suit:
            if self.value <= c2.value:
                return True
            else:
                return False
        return False

    def __ge__(self, c2):
        if self.suit >= c2.suit:
            return True
        if self.suit == c2.suit:
            if self.value >= c2.value:
                return True
            else:
                return False
        return False

    def __eq__(self, c2):
        return (self.suit == c2.suit) and (self.value == c2.value)

    def __repr__(self):
        return str(self.values[self.value]) + " " + str(self.suits[self.suit][0])