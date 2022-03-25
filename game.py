from random import randint

from gameComponents import gameVars, winLose, myFunction

while gameVars.player_choice is False:
    print("============================^_____________^============================")
    print("                                                                      =")
    print("= ************************ RPS GAME in TEXT ************************* =")
    print("=                                                                     =")
    print("=                        Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives, "                       =")                     
    print("=                        Player Lives:", gameVars.player_lives, "/", gameVars.total_lives, "                         =")
    print("=                                                                     =")
    print("============================================================*~*==xoxo==")

    print("Choose your favorite weapon! Or type quit to exit\n")
    gameVars.player_choice = input ("Choose rock, paper, scissors: \n")

    myFunction.function()
        
    if gameVars.player_lives == 0:
        winLose.winorlose("Lost")
    if gameVars.computer_lives == 0:
        winLose.winorlose("Won")

    print("Player Lives: ", gameVars.player_lives)
    print("Computer Lives: ", gameVars.computer_lives)

    gameVars.player_choice = False






    