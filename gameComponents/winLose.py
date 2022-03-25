from gameComponents import gameVars

def winorlose(status):
    print("=======^o^======= You", status, "! Do you wanna play it again? ======^o^======")
    choice = input("Y / N?")

    if choice == "N" or choice == "n":
        print("You wanna quit? Let's play next time!")
        exit()
    elif choice == "Y" or choice == "y":

        gameVars.player_lives = gameVars.total_lives
        gameVars.computer_lives = gameVars.total_lives
        gameVars.player_choice = False
    else:
        print("Make a valid choice - Y or N")
        choice = input ("Y / N?")