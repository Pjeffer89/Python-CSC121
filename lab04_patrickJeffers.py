# Patrick Jeffers   Lab04   8/26/2021
# This program is based on chapter 3 exercise number 13 from the book.  This
# program calculates shipping charges for the user based on the users input.  It
# calculates by different tiers of weight ranges.

# Program constants.
#   Weight breaks.
TOPWEIGHT = 10;
SECONDWEIGHT = 6;
THIRDWEIGHT = 2;
BOTTOMWEIGHT = 0;
#   Weight charges.
TOPCHG = 5.25;
SECONDCHG = 4.35;
THIRDCHG = 3.75;
BOTTOMCHG = 2.25;

# Local variables.
weight = 0.0;
shippingCost = 0.0;

# Input, get weight from user keyboard as a float type.
weight = float(input('Please enter the weight of the package: '))

# Process, calculates the shipping charges based on previous user input.
if weight > TOPWEIGHT:
    shippingCost = TOPCHG
elif weight > SECONDWEIGHT:
    shippingCost = SECONDCHG
elif weight > THIRDWEIGHT:
    shippingCost = THIRDCHG
else: shippingCost = BOTTOMCHG

# Output, displays results back to user.
print('Weight of package is ', format(weight,'.2f'))
print('Shipping charge: $', format(shippingCost*weight,'.2f'))
