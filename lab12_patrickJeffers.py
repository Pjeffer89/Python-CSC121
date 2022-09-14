# Patrick Jeffers   Lab12   9/24/2021
# Based on chapter 5 exercise 19 from the book.  This program calculates the 
# future value of a savings account with input given by the user.  The program 
# accepts the current value, the interest rate and number of months in the 
# account, then calculates and displays the future value.  Then allows the user
# to continue making calculations as needed.

# Variables/CONSTANTS, declared and initialized.
futureValue = 0.0
presentValue = 0.0
interestRate = 0.0
numOfMonths = 0

# The main function of the program.  Calls the other functions.
def main():
    loopControl = 'Y'                           
    while loopControl == 'Y' or 'y':                        # Allows for looping
        presentValue, interestRate, numOfMonths = inputData()
        futureValue = calcFutureValue(presentValue, interestRate, numOfMonths)
        printResults(presentValue, interestRate, futureValue)
        loopControl = input('Do you want to calculate another? (Y/N): ')
        if loopControl != 'Y':
            break                                                  # Breaks Loop
        print('')
        
# Input. This function is used to gather the information needed from the user.    
def inputData():
    presentValue = float(input("Please enter the current value" \
                               " of the account: "))
    interestRate = float(input("Please enter the monthly interest rate " \
                               "percentage: "))
    numOfMonths = int(input("Please enter the number of months that the " \
                            "money will be left in the account: "))
    return presentValue, interestRate, numOfMonths
    
# Process. This function makes the calculations and returns the future value.
def calcFutureValue(pVal, iRate, numMonths):
    rateAsDecimal = (iRate / 100)
    fValue = pVal * ((1 + rateAsDecimal) ** (numMonths))
    return fValue

# Output. This function outputs certain information as well as the results of
# the calculation back to the user.
def printResults(pVal, iRate, fVal):
    print('')
    print('Present Value: $', f'{pVal:,.2f}', sep = '')
    print('Interest Rate : ', f'{iRate:,.2f}', '%', sep = '')  
    print('Future Value: $', f'{fVal:,.2f}', sep = '')
    print('')
    
# Calling the main function.
main()