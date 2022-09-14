# Patrick Jeffers   Lab17   11/1/2021
# The program takes an input from the user and determines whether it is a number
# or not. Then reports the information back to the user. This program is a 
# demonstration of exception handling and error management.

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    theNumber = " "     # Declares variable for coming user input, sets up loop.
    while theNumber:
        theNumber = input("Please enter the number or press enter to end: ")
        if (theNumber == ""):
            print("Program ended.")
            break
        isNumeric = isNumber(theNumber) #Calls test function passing user input.
               
# This function tests to see if the value is numeric.       
def isNumber(n):
    try:
        num = float(n)                                    # Converts to a float.
        print("This is a valid number.")
        print("")
    except:                      # Displays if conversion was unable to process.
        print("This is not a valid number.")
        print("")

# Calling the main function to start the program.
main()