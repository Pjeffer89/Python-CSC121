# Patrick Jeffers   Lab13   9/29/2021
# Chapter 5 exercise 20.  This program creates a number guessing game.  The 
# computer generates a number from 1-100 and allows the player to try and guess
# it.  The game hints for low or high guesses as well as tracks guesses, 
# allowing up to 7 before player loses.  The total wins and losses are also 
# tracked and displayed when the game is exited.  The game allows a value to be
# entered for the player to stop playing.

# Imports the random function to be used to generate a number.
import random

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    gameWon = False                         #Variables declared and initialized.
    newGame = True
    wins = 0
    losses = 0
    playerNum = 0
    randomNum = 0
    
    while newGame or gameWon:  # Starts the game. Controlling variables for run.
        if playerNum == 111:         # Ends loop in player has entered sentinel.
            break
        numGuesses = 0                        # Sets the number of guesses to 0.
        randomNum = createRandomNumber()
        print("Guess The Number Game")
        playerNum = getPlayerNum()        # Gets the guessed number from player.
        if playerNum == 111:  # Allows player to quit then displays wins/losses.
            displayWinsLosses(wins, losses)
            break
        numGuesses = numGuesses + 1                   # Logs first player guess.
        remainingGuesses = (7 - numGuesses)   # Tracks remaining guesses from 7.
        result = isNumCorrect(playerNum, randomNum)    # Evaluates player guess.
    
        # This loop runs when the initial guess was incorrect.
        while result != ("Congratulations, you got it right!"):
            print(result)                # Prints whether guess was high or low.
            print("Remaining Guesses: ", remainingGuesses) # Display guess tally
            playerNum = getPlayerNum()              # Get new guess from player.
            if playerNum == 111:   # Allows player to exit, then displays score.
                displayWinsLosses(wins, losses)
                newGame = False        # These set to false to stop program from
                gameWon = False        # running again.
                break            
            numGuesses = numGuesses + 1                 # Tallies another guess.
            remainingGuesses = (7 - numGuesses)# Tracks remaining guesses from 7
            if remainingGuesses < 0:     # Player loses when no guesses remain.
                losses = losses + 1             # Tally a loss and restart game.
                print("Sorry, you lost this match. Try Again.")
                print()
                break
            result = isNumCorrect(playerNum, randomNum)    # Evaluates guess for
                                                           # loop control.
        # Runs if player guesses the number correctly.
        if result == ("Congratulations, you got it right!"):
            print(result)                        # Print congratulatory message.
            print("It took you ", numGuesses, "guesses.") # Display the number
            print()                                 # of guesses used by player.
            wins = wins + 1                        # Tally a win for the player. 
            gameWon = True                        # Assures restart of new game.


# Closing output to display final win/loss count.
def displayWinsLosses(wins, losses):
    print("Thanks for playing!")
    print("Wins: ", wins)
    print("Losses: ", losses)
    print()

# Generates the random number that the player is trying to guess.
def createRandomNumber():
    randomNum = random.randint(1, 100)      # Generate random number from 1-100.
    return randomNum

# This function gets a number or guess from the player.
def getPlayerNum():
    playerNum = int(input("Guess a number from 1-100, or 111 to exit: "))
    return playerNum

# Evaluates if the players entered number is correct, high, or low.
def isNumCorrect(playerGuess, correctNum):
    if playerGuess > correctNum:
        result = ("Too high, try again.")
        return result
    
    elif playerGuess < correctNum:
        result = ("Too low, try again.")
        return result
    else:
        result = ("Congratulations, you got it right!")
        return result

main()                                                              # Calls main
