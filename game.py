from random import randint

from gameComponents import gameVars, winLose

while gameVars.player_choice is False:
    print("============================^_____________^============================")
    print("=                        ~* RPS GAME in TEXT *~                       =")
    print("=                                                                     =")
    print("=                    Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)                      =")
    print("=                    Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)                      =")
    print("=                                                                     =")
    print("============================================================*~*==xoxo==")

    print("Choose your favorite weapon! Or type quit to exit/n")
    gameVars.player_choice = input ("Choose rock, paper, scissors: \n")

    if gameVars.player_choice == "quit":
        print("You want to quit")
        exit()

    print("You chose: " + gameVars.player_choice)

    gameVars.computer_choice = gameVars.choices[randint(0,2)]

    print("Computer chose: " + gameVars.computer_choice)

    if gameVars.computer_choice == gameVars.player_choice:
        print("Tie ^_^||")

    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            print("You Lose! So bad...")
            gameVars.player_lives -= 1
        else:
            print("You WIN!!!")
            gameVars.computer_lives -= 1

    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "scissors":
            print("You WIN!!! OKAY!!")
            gameVars.computer_lives -= 1
        else:
            print("You Lose! Feel bad for you...")
            gameVars.player_lives -= 1

    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
            print("You Lose! No problem, everyone loses many time in life time!")
            gameVars.player_lives -= 1
        else:
            print("You WIN!! YEAH!!!")
            gameVars.computer_live -=1
        
    if gameVars.player_lives == 0:
        winLose.winorlose("Lost")
    if gameVars.computer_lives == 0:
        winLose.winorlose("Won")

    print("Player Lives: ", gameVars.player_lives)
    print("Computer Lives: ", gameVars.computer_lives)

    gameVars.player_choice = False






    