''' Python program to play a game of rock paper and scissors
    Author: srikanth'''

import random  #importing random library
f = "1"        #flag
while f == "1":
    player = input("Enter R for rock , P for paper and S for scissors : ")
    player = player.upper()   #converts to uppercase if the input was in lower case.
    computer = random.choice(['R','P','S'])  
    if (player == computer):
        print("both chose", player,"draw match.")
    elif( player == "R" and computer == "S" ) or ( player == "P" and computer == "R" ) or ( player == "S" and computer == "P" ):
        print("player wins.", player, "defeats", computer)
    else:
        print("computer wins.",computer, "defeats", player)
    f=input(" press 1 to play again or press  any other key to quit : ")
    if (f == "1"):   #check flag variable
        continue
    else:
        print("thanks for playing :")
