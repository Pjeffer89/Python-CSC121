# Patrick Jeffers   Lab02   8/19/2021
# This program allows the user to play rock, paper, scissors with the computer.
# The assignment was to rewrite the code more efficiently, minimizing the number
# of "decisions" required to play the game.


# Used to generate random numbers for computer selections.
import random

# Program constants.
ROCK=1 ; PAPER=2; SCISSORS=3

# Start game, create and assign variables to get computer and player selections.
comp=random.randint(1,3)
player=int(input('Enter your choice \n'
'1 = Rock \n'
'2 = Paper \n'
'3 = Scissors \n'))

# Creates 2 variables to store correlating string values based on computer and 
# player selections.  Then assigns these based on the selections above.  This is
# used for display later.
if comp == ROCK:
    compChoice = 'Rock'
elif comp == PAPER:
    compChoice = 'Paper'
else: compChoice = 'Scissors'
if player == ROCK:
    playerChoice = 'Rock'
elif player == PAPER:
    playerChoice = 'Paper'
else: playerChoice = 'Scissors'

# Displays choices of player and computer.
print('Computer chose: ', compChoice)
print('Player chose: ', playerChoice)

# Determines winner and displays results.
if comp == player:
    print('Tie game')
elif comp == ROCK:
    if player == PAPER:
        print('Player won')
    else:
        print('Computer won')
elif comp == PAPER:
    if player == SCISSORS:
        print('Player won')
    else:
        print('Computer won')
elif comp == SCISSORS:
    if player == ROCK:
        print('Player won')
    else:
        print('Computer won')