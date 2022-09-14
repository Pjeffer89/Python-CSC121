# Patrick Jeffers   Lab19   11/8/2021
# Based on chapter 7 exercise 8 in the book.  This program pulls names from 2 
# files and puts them into lists.  The program then allows you to search by 
# gender for popular names from the lists.  After each iteration a message of
# whether the name or names was found will be displayed. To stop the program, 2
# NULL entries are entered.  After ending the program a total of the names 
# searched for and found will be displayed. 


# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    nameSearch = True                      # Variables declared and initialized.
    boyNamesTested = 0
    girlNamesTested = 0
    boyNamesListed = 0
    girlNamesListed = 0
    
    heading()                              # Displays a heading for the program.
    boyNames = getBoyNamesFromFile()                # Gets boys names from file.
    girlNames = getGirlNamesFromFile()             # Gets girls names from file.

    while nameSearch == True:            # Loop for allowing more name searches.
        print('')
        boySearch = input('Please enter a boys name: ') #Getting names to search
        girlSearch = input('Please enter a girls name: ')           # from user.
        print('')
    
        # This section calls the functions to evaluate if the names are listed.
        # Only when entry is not NULL. Also accumulates tested and listed names.
        if boySearch != '':
            boyNamesListed = isItABoyName(boySearch, boyNames, boyNamesListed)
            boyNamesTested += 1                                    # Accumulator
        if girlSearch != '':
            girlNamesListed =isItAGirlName(girlSearch,girlNames,girlNamesListed)
            girlNamesTested += 1                                   # Accumulator
        if boySearch == '' and girlSearch == '':    # Ends program when 2 NULLs.
            nameSearch = False
            print('No names entered, program ended.')    # Displays final count.
            print('')
            print('Boys names tested: ' + format(boyNamesTested))
            print('Girls names tested: ' + format(girlNamesTested))
            print('Boys names found in list: ' + format(boyNamesListed))
            print('Girls names found in list: ' + format(girlNamesListed))
         

# Function to display heading for the program.
def heading():
    print("Enter names to see if they were popular during the early 2000's.")
    print("Enter either a boys name or a girls name.  Enter 2 blank entries "\
          "to end the program.")

# Function to evaluate if boys name is listed in list.  Displays appropriate 
# message and accumulates when necessary. Returns accumulated total.
def isItABoyName(boySearch, boyNames, boyNamesListed):
    if boySearch in boyNames:
        print(f'{boySearch} was found among popular names.')
        boyNamesListed += 1
    else: 
        print(f'{boySearch} was not a popular name.')
    return boyNamesListed

# Function to evaluate if girls name is listed in list.  Displays appropriate 
# message and accumulates when necessary. Returns accumulated total.        
def isItAGirlName(girlSearch, girlNames, girlNamesListed):
    if girlSearch in girlNames:
        print(f'{girlSearch} was found among popular names.')
        girlNamesListed += 1
    else: 
        print(f'{girlSearch} was not a popular name.')
    return girlNamesListed
    
# Function to read boys names from file and put into list.
def getBoyNamesFromFile():
    infileBoys = open('BoyNames.txt', 'r')
    boyNames = infileBoys.readlines()
    infileBoys.close()
    for index in range(len(boyNames)):
        boyNames[index] = boyNames[index].rstrip('\n')
    return boyNames

# Function to read girls names from file and put into list.
def getGirlNamesFromFile():
    infileGirls = open('GirlNames.txt', 'r')
    girlNames = infileGirls.readlines()
    infileGirls.close()
    for index in range(len(girlNames)):
        girlNames[index] = girlNames[index].rstrip('\n')
    return girlNames    
    
# Calls main to start program.
main()