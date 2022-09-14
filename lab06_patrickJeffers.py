# Patrick Jeffers   Lab06   9/3/2021
# Chapter 3 exercise 16.  This program takes a year entered by the user and 
# determines if that year is a leap year or not.  Then the program displays the
# correct number of days in February of the entered year.

# Variables, declared and initialized.
year = 0;
days = 0;

# Input, gets the year from the user.
year = int(input("Enter a year: "))

# Process.  First determines if the year is divisible by 100 and if so is it 
# also divisible by 400.  If both then its a leap year.  Then if the year is not
# divisible by 100, if the year is divisible by 4 it is a leap year.  Days are 
# then assigned either to 29 or 28 accordingly. 
if year % 100 == 0:
    if year % 400 == 0:
        days = 29
    else: days = 28
elif year % 4 == 0:
    days = 29
else: days = 28
        
# Output, displays the number of days in February of the entered year back to 
# the user.
print("In " + format(year) + " February has " + format(days) + " days.")