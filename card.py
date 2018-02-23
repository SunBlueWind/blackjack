import time
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank;
        self.suit = suit;
    def __repr__(self):
        return f"({self.rank}, {self.suit})"

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in range(1,14) for suit in ("Hearts", "Diamonds", "Spades", "Clubs")]
        self.count = 52

    def __repr__(self):
        return f"{self.cards}"

    def __len__(self):
        return self.count

    def shuffle(self):
        print("Shuffling cards...\n")
        time.sleep(2)
        random.shuffle(self.cards)
        return

    def pop_top(self):
        top = self.cards.pop(0)
        self.count -= 1
        return top

    def reset(self):
        self.cards.clear()
        self.cards = [Card(rank, suit) for rank in range(1,14) for suit in ("Hearts", "Diamonds", "Spades", "Clubs")]
        self.count = 52
        return
