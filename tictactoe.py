board = {"position 1":2, "position 2": 3,"position 3": 
         4,"position 4": 5,"position 5": 6,"position 6":
        7,"position 7": 8,"position 8": 9,"position 9": 10, }
print (board)
global playerselection
playerselection = 0
play = True
def playerselect():
    global playerselection
    print(f"Pick a position player {playerselection}")
    playerchoice = input()
    if playerchoice == "2" and board["position 1"] == 2:
        board["position 1"] = playerselection
        print(board)
        if playerselection == 0:
            playerselection = 1
        else:
            playerselection = 0
    elif playerchoice == "3" and board["position 2"] == 3:
        board["position 2"] = playerselection
        print(board)
        if playerselection == 0:
            playerselection = 1
        else:
            playerselection = 0
    elif playerchoice == "4" and board["position 3"] == 4:
        board["position 3"] = playerselection
        print(board)
        if playerselection == 0:
            playerselection = 1
        else:
            playerselection = 0
    elif playerchoice == "5" and board["position 4"] == 5:
        board["position 4"] = playerselection
        print(board)
        if playerselection == 0:
            playerselection = 1
        else:
            playerselection = 0
    elif playerchoice == "6" and board["position 5"] == 6:
        board["position 5"] = playerselection
        print(board)
        if playerselection == 0:
            playerselection = 1
        else:
            playerselection = 0
    elif playerchoice == "7" and board["position 6"] == 7:
        board["position 6"] = playerselection
        print(board)
        if playerselection == 0:
            playerselection = 1
        else:
            playerselection = 0
    elif playerchoice == "8" and board["position 7"] == 8:
        board["position 7"] = playerselection
        print(board)
        if playerselection == 0:
            playerselection = 1
        else:
            playerselection = 0
    elif playerchoice == "9" and board["position 8"] == 9:
        board["position 8"] = playerselection
        print(board)
        if playerselection == 0:
            playerselection = 1
        else:
            playerselection = 0
    elif playerchoice == "10" and board["position 9"] == 10:
        board["position 9"] = playerselection
        print(board)
        if playerselection == 0:
            playerselection = 1
        else:
            playerselection = 0

def loop():
    while play == True:
        playerselect()
        wincheck()

def wincheck():
    if board["position 1"] == board["position 2"] == board["position 3"]:
        print(f"Player {board['position 1']} wins!")
        play = False
    elif board["position 4"] == board["position 5"] == board["position 6"]:
        print(f"Player {board['position 4']} wins!")
        play = False
    elif board["position 7"] == board["position 8"] == board["position 9"]:
        print(f"Player {board['position 7']} wins!")
        play = False
    elif board["position 1"] == board["position 4"] == board["position 7"]:
        print(f"Player {board['position 1']} wins!")
        play = False
    elif board["position 2"] == board["position 5"] == board["position 8"]:
        print(f"Player {board['position 2']} wins!")
        play = False
    elif board["position 3"] == board["position 6"] == board["position 9"]:
        print(f"Player {board['position 3']} wins!")
        play = False
    elif board["position 1"] == board["position 5"] == board["position 9"]:
        print(f"Player {board['position 1']} wins!")
        play = False
    elif board["position 3"] == board["position 5"] == board["position 7"]:
        print(f"Player {board['position 3']} wins!")
        play = False
    if board["position 1"] != 2 and board["position 2"] != 3 and board["position 3"] != 4 and board["position 4"] != 5 and board["position 5"] != 6 and board["position 6"] != 7 and board["position 7"] != 8 and board["position 8"] != 9 and board["position 9"] != 10:
        print("It's a draw!")
        play = False



playerselect()

loop()
wincheck()

    

