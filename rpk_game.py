# Project 3 by Kylie Ying - Rock Paper Scissors

import random

# The user inputs their own value into the and the comptuer will generate a random one using the choice function.

def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

# If the two variables are equal in value it's a tie

    if user == computer:
        return 'It\'s a tie'

# If the is_win funciton is true then then it is a win for the user, else it is a win for the computer.

    if is_win(user, computer):
        return 'You won!'
    return 'You lost!'
    
# Conditions are set to determine if the player wins.

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    
print(play())