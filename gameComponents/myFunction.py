
from random import randint

from gameComponents import gameVars

def function():

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
            print("You WIN!!! Oh, I'm gonna be mad on you")
            gameVars.computer_lives -= 1

    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "scissors":
            print("You WIN!!! OKAY!! NOT BAD!!")
            gameVars.computer_lives -= 1
        else:
            print("You Lose! Sorry, feel bad for you :)")
            gameVars.player_lives -= 1

    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
            print("You Lose! No problem, everyone loses many times in life time!")
            gameVars.player_lives -= 1
        else:
            print("You WIN!! YEAH!!!")
            gameVars.computer_lives -= 1