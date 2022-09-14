# Patrick Jeffers   Lab16   10/4/2021
# Based on chapter 6 exercise 8 in the book.  This program reads from a file of
# random numbers created by the program in Lab15.  This program reads and prints
# the numbers from the file.  Additionally the program calculates and displays
# the sum of the numbers, the average of the numbers, the quantity of numbers in
# the file, the smallest and the largest number.

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    readFile("randomNumbers.txt")
    
# This function takes a total and quantity then calculates and returns the
# average.
def avgNums(total,numOfNumbers):
    avgOfNums = (total / numOfNumbers)
    return avgOfNums

# This function accesses the file, processes file and results and displays back
# to the user when called by main.
def readFile(earlierFile):
    theFile = open(earlierFile, "r")                               # Opens file.
    sumOfNums = 0                  # Declaring and initializing local variables.
    numberOfNums = 0
    avgOfNums = 0
    minNum = 0
    maxNum = 0
    listOfNums = []
    print("Random Numbers")                         # Prints heading for output.
    print("--------------")
    line = theFile.readline()                # Reads the first line in the file.
    while line != '':           # Used to read each line that contains a number.
        eachNum = int(line) #Converts to int, and assigns the line to a variable
        listOfNums.append(eachNum)    # Creates list and adds each number to it.
        sumOfNums += eachNum         # Accumulator to total all numbers in file.
        numberOfNums += 1              # Counts the quantity of numbers in file.
        avgOfNums = avgNums(sumOfNums,numberOfNums)   # Call to get avg of nums.
        minNum = min(listOfNums)        # Finds and assigns the smallest number.
        maxNum = max(listOfNums)         # Finds and assigns the largest number.
        print(eachNum)                # Prints each number as the loop iterates.
        line = theFile.readline()    # Reads the next line for the while loop to 
                                     # interpret.
  # Outputs the processed numbers back to the user.  
    print("--------------")
    print("The sum of all random numbers is: " + f'{sumOfNums:,.0f}')
    print("The quantity of numbers in the file is: " + f'{numberOfNums:,.0f}')
    print("The average of the numbers is: " + f'{avgOfNums:,.2f}')
    print("The smallest number is: " + f'{minNum}')
    print("The largest number is: " + f'{maxNum}')
    print("-------------------------------------------")
    
# Calls main to start program.
main()