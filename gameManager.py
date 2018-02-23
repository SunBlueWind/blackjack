import player
import messenger
import utils

class GameManager:
    def __init__(self):
        self.dealer = player.Dealer()
        self.players = []
        self.msgr = messenger.Messenger()

    def __repr__(self):
        ret = repr(self.dealer) + '\n'
        for p in self.players:
            ret += repr(p) + '\n'
        return ret

    def play(self):
        self.init_players()
        while True:
            self.init_bet()
            self.init_deal_cards()
            self.show_cards()
            self.hit()
            self.play_dealer()
            self.adjust_chips()
            self.check_broke()
            if len(self.players) < 1:
                break
            if self.dealer_broke() or not utils.replay():
                break
            self.reset()
        return

    def init_players(self):
        plys = self.msgr.init_players()
        for p in plys:
            self.players.append(player.Player(p))
        return

    def init_deal_cards(self):
        self.dealer.shuffle()
        self.deal_cards()
        self.deal_cards()
        return

    def init_bet(self):
        self.msgr.bet(self.players)
        return

    def deal_cards(self):
        self.dealer.receive_card(self.dealer.deal())
        for p in self.players:
            p.receive_card(self.dealer.deal())
        return

    def show_cards(self):
        self.msgr.show(self.dealer, self.players)
        return

    def hit(self):
        for p in self.players:
            self.msgr.hit(p, self.dealer)
        return

    def play_dealer(self):
        self.msgr.play_dealer(self.dealer)
        return

    def adjust_chips(self):
        self.dealer.adjust_chips(self.players)
        self.msgr.show_results(self.dealer, self.players)
        return

    def check_broke(self):
        self.players[:] = [p for p in self.players if p.chips > 0]
        return

    def dealer_broke(self):
        if self.dealer.chips <= 0:
            return True
        return False

    def reset(self):
        self.dealer.reset()
        for p in self.players:
            p.reset()
        return
