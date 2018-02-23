import time
import utils

class Messenger:
    ''' Messenger is responsible for game input and output '''
    def __init__(self):
        print("\n********************************")
        print("****  Welcome to Blackjack  ****")
        print("********************************\n")
        return

    def __del__(self):
        print("\n*********************************")
        print("*******     Game Over     *******")
        print("*********************************\n")

    def init_players(self):
        while True:
            num = utils.getPositiveInt("Please Enter the Number of Players: ")
            if num > 7:
                print("*** Sorry we only have enough cards for 7 players at most.")
            else:
                break
        players = []
        print("*** Please Ensure All Players Have Unique Names ***")
        for i in range(num):
            p = input(f"Please Enter the Name of Player {i+1}: ")
            players.append(p)
        return players

    def bet(self, players):
        for p in players:
            while True:
                num = utils.getPositiveInt(f"{p.name}, please enter your bet (you have {p.chips} chips left): ")
                try:
                    p.bet(num)
                except ValueError as e:
                    print(f"*** {e}")
                else:
                    break
        return

    def show(self, dealer, players):
        print(f"Dealer: (***,***) {dealer.hand.cards[1]}\n")
        for p in players:
            time.sleep(1)
            print(f"{p.name}: {p}\n")
        print("=====================================\n")
        return

    def hit(self, player, dealer):
        time.sleep(1)
        print(f"{player.name}; {player}\n")

        while not player.hand.is_busted():
            if utils.doHit(player):
                print("Dealing...\n")
                time.sleep(1)
                player.receive_card(dealer.deal())
                print(f"{player.name}: {player}\n")
            else:
                break

        if player.hand.is_busted():
            time.sleep(1)
            print(f"{player.name} has gone busted!\n")
        print("=====================================\n")
        return

    def play_dealer(self, dealer):
        time.sleep(1)
        print("Now Playing Dealer's Hand...\n")
        time.sleep(1)
        print(f"{dealer.name}: {dealer}\n")

        while dealer.hand.best_total() < 17:
            time.sleep(1)
            dealer.receive_card(dealer.deal())
            print(f"{dealer.name}: {dealer}\n")

        if dealer.hand.is_busted():
            time.sleep(1)
            print("Dealer has gone busted!\n")
        print("=====================================\n")
        return

    def show_results(self, dealer, players):
        time.sleep(1)
        if dealer.chips < 0:
            print("*** Game Over. The Dealer is broke. ***\n")
            return
        print("Current Balance:\n")
        for p in players:
            if p.chips <= 0:
                print(f"{p.name} is broke.\n")
            else:
                print(f"{p.name}: {p.chips}\n")
        return
