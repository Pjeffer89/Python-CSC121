# Patrick Jeffers   Lab01   8/18/2021
# Instructions
# This program accepts a numeric grade input and processes it into a letter
# grade. Then outputs the results based on the number entered.  The lab 
# instructions were to take existing code and rewrite it to be more neat and
# efficient.  

# Input, declaring/initializing the variable and getting input from the user.
grade=float(input('Enter the students test grade. '))

# Processing the numeric grade into a letter grade, then outputs the result
# based on score.
if grade>=90:   
    print('\nTest grade is a(n) ','A')
elif grade>=80:
    print('\nTest grade is a(n) ','B')    
elif grade>=70:
    print('\nTest grade is a(n) ','C')
elif grade>=60:
    print('\nTest grade is a(n) ','D')
else:
    print('\nTest grade is a(n) ','F')

# Closing message for user.
print('\nThanks for using the letter grade calculator.')