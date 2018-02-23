class Hand:
    def __init__(self, cards):
        total = 0
        for c in cards:
            if c.rank == 11 or c.rank == 12 or c.rank == 13:
                total += 10
            else:
                total += c.rank
        self.cards = cards
        self.softTotal = total

    def __repr__(self):
        return f"Cards: {self.cards}. Soft Total: {self.softTotal}. Best Total: {self.best_total()}"

    def is_busted(self):
        return self.softTotal > 21

    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 11 or card.rank == 12 or card.rank == 13:
            self.softTotal += 10
        else:
            self.softTotal += card.rank
        return

    def best_total(self):
        total = self.softTotal
        for c in self.cards:
            if c.rank == 1 and total <= 11:
                total += 10
        return total

    def reset(self):
        self.cards.clear()
        self.softTotal = 0
        return
