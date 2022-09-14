# Patrick Jeffers   Lab08   9/20/2021
# Based on chapter 4 exercise 6 from the book. This program prompts the user for
# which way they wish to convert Fahrenheit and Celsius. Then asks for a range
# of temperatures to convert between.  Once all user input is collected the 
# program makes the appropriate conversion and displays the results neatly in a
# table.

# Variables, declared and initialized.
celsiusTemp = 0;
fahrenheitTemp = 0;
convChoice = 0;
lowNum = 1;
highNum = 1;


# Input.  This loop allows the user to continue making conversions until 0 and 0
# are entered for the temperature range. User input is gathered below.
while True:
        if lowNum == 0 and highNum == 0:
                break
        convChoice = int(input("Would you like to convert " + \
                           "Celsius to Fahrenheit or"+'\n'
                       "Fahrenheit to Celsius?"+'\n''\n'
                       "\t1. Celsius to Fahrenheit"+'\n'
                       "\t2. Fahrenheit to Celsius"+ '\n''\n'
                       "Please select from the options above: "));
        print('To end the program enter 0 and 0 for the temperature range');
        lowNum = int(input("Enter the beginning or lowest temperature" + \
                           " in the range: "))
        highNum = int(input("Enter the final or highest " + \
                        "temperature in the range: "))

        if (convChoice == 1):                   # Process and Output for C to F.
                print ('\n' + "Celsius" + '\t''\t' + "Fahrenheit");
                print('---------------------------');
                for celsiusTemp in range (lowNum, (highNum + 1)):
                        fahrenheitTemp = ((9 / 5) * celsiusTemp) + 32;
                        print (celsiusTemp, '\t''\t', \
                               format(fahrenheitTemp,".2f"));
                print('\n');

        elif (convChoice == 2):                 # Process and Output for F to C.
                print ('\n' + "Fahrenheit" + '\t' + "Celsius");
                print('------------------------');
                for fahrenheitTemp in range (lowNum, (highNum + 1)):
                        celsiusTemp = ((5/9) * (fahrenheitTemp - 32));
                        print (fahrenheitTemp, '\t''\t', \
                               format(celsiusTemp,".2f"));
                print('\n');
        
        else:
                print('\n');
                print('Please select a valid conversion option from the menu.');
                print('\n');