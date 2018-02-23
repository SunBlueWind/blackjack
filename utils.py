def getPositiveInt(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print("*** An Error Occured. Try Again.")
        else:
            if num < 1:
                print("*** Number Must be Positive. Try Again.")
                continue
            return num

def doHit(player):
    while True:
        ans = input(f"{player.name}, do you want to Hit or Stand? (H/S): ")
        print("")
        if ans.lower().startswith("h"):
            return True
        elif ans.lower().startswith("s"):
            return False
        else:
            print("*** Invalid Input. Try Again\n")

def replay():
    while True:
        ans = input("Do you want to Continue? (Y/N): ")
        print("")
        if ans.lower().startswith("y"):
            return True
        elif ans.lower().startswith("n"):
            return False
        else:
            print("*** Invalid Input. Try Again\n")
