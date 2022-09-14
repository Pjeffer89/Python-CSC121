# Patrick Jeffers   Lab15   10/4/2021
# Based on chapter 6 exercise 7 in the book.  This program prompts the user for 
# how many numbers they would like to generate.  Then the program creates this 
# many random numbers between 1-500.  The program then creates a text file and
# stores the random numbers in the new file.

# Imports the random function to be used to generate a number.
import random

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    quantityOfNums = getQuantityOfNums()# Gets the quantity of numbers to create
    newFile = open("randomNumbers.txt", "w")           # Opens/Creates the file.

    for randomNums in range(1, quantityOfNums + 1):   # Loops based on quantity.
        randomNum = getRandomNum()          # Generates random number each time.
        newFile.write(f'{randomNum}\n')       # Writes new random number to file
                                               # with added new line formatting.
   
# This function gets the quantity of numbers to generate from the user.
def getQuantityOfNums():
    quantityOfNums = int(input("How many numbers would you like to create?: "))
    return quantityOfNums

# This function generates a random number between 1-500 when called.
def getRandomNum():
    randomNum = random.randint(1,500)
    return randomNum

# Calls main.
main()