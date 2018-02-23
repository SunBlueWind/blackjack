import hand
import card

class Player:
    def __init__(self, name):
        self.chips = 1000
        self.name = name
        self.currentBet = 0
        self.hand = hand.Hand([])

    def __str__(self):
        ret = ""
        for c in self.hand.cards:
            ret += str(c) + ' '
        return ret

    def __repr__(self):
        return f"{self.name}: {self.chips} left. Bet: {self.currentBet}. {self.hand}"

    def win(self):
        self.chips += self.currentBet * 2
        return

    def win_double(self):
        self.chips += self.currentBet * 3
        return

    def bet(self, val):
        ''' Will raise exception if not enough chips are left '''
        if (val > self.chips):
            raise ValueError(f"{self.name} only has {self.chips} chip(s) left. Cannot bet {val} chip(s).")
        else:
            self.chips -= val
            self.currentBet += val
        return

    def receive_card(self, card):
        self.hand.add_card(card)
        return

    def reset(self):
        self.hand.reset()
        self.currentBet = 0
        return

class Dealer(Player):
    def __init__(self):
        Player.__init__(self, "Dealer")
        self.chips = 10000
        self.deck = card.Deck()

    def shuffle(self):
        self.deck.shuffle()
        return

    def deal(self):
        return self.deck.pop_top()

    def reset(self):
        super().reset()
        self.deck.reset()
        return

    def adjust_chips(self, players):
        for p in players:
            if p.hand.best_total() == 21:
                self.chips -= p.currentBet * 2
                p.win_double()
            elif not p.hand.is_busted() and \
                (self.hand.is_busted() or self.hand.best_total() < p.hand.best_total()):
                self.chips -= p.currentBet
                p.win()
            else:
                self.chips += p.currentBet
        return
