# Patrick Jeffers   Lab09   9/21/2021
# Based on chapter 4 exercise 7 in the book.  This program calculates pay for a 
# scenario where someone would make a penny on day 1 then 2 pennies day 2 then 
# continues to double.  The program allows the user to enter the number of days 
# worked then calculates through that many iterations.  The program also will 
# provide a total or a table of each days pay based on user choice.

# Variables/CONSTANTS, declared and initialized.
daysWorked = 1;
day = 0;
pennies = 0;
totalPennies = 0;
totalPay = 0.0;
dollars = 0.0;
dayPayOrTotal = 0;
PENNY = 0.01;

# Input.  This first bit (loop) keeps the program running until the user enters
# a 0 for the number of days worked.  Following that is another input to allow 
# the user to pick a table output or just a total from a menu.
while daysWorked != 0:
    daysWorked = int(input("Please enter the number of days worked, " + \
                           "or 0 to exit: "));
    if daysWorked == 0:
        break;
    dayPayOrTotal = int(input("Do you want to display each days pay or " \
                        "just the total? " + '\n' +
                        '\t' + "1: Each days pay." + '\n' +
                        '\t' + "2: Just the total." + '\n' +
                        "Select from the menu above: "));
# Process and output for if the user wishes to see a table of each days pay.
    if (dayPayOrTotal == 1):
        print ('\n', "Day", '\t', "Pay", sep = '');                    # Heading
        print('-----   ------');
        for day in range(daysWorked):                                  # Process
            pennies = (2 ** day);
            dollars = pennies * PENNY;                          # For formatting
            print(day + 1, '\t',"$" ,f'{dollars:,.2f}', sep = '');      # Output
        print("");
# Process and output for if the user wishes to see just the combined total pay.        
    elif (dayPayOrTotal == 2):
        for day in range(daysWorked):                                  # Process
            pennies = (2 ** day);
            totalPennies = (totalPennies + pennies);
            dollars = pennies * PENNY;
        totalPay = (totalPennies * PENNY);                # Calculates the total
        print('\n', "Total Pay: $", f'{totalPay:,.2f}', '\n', sep = '');# Output
        print(""); 
        totalPennies = 0;               # Resets this variable to 0 so that it 
                                        # won't keep adding to future iterations
                                        # of the loop.
                                        