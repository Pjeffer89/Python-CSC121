# Patrick Jeffers   Project 1   9/13/2021
# This program takes room dimensions and shade characteristics from the user.  
# This data is then used to calculate the area of the room and the required 
# BTU capacity needed of the rooms air conditioner.

# Variables, (all lengths are in feet / area in sqft.)
roomLength = 0.0;
roomWidth = 0.0;
roomArea = 0.0;
shadeAmt = 0;
btu = 0.0;
shadeAsString = "";

# Constants
CAPACITYHEADING = "Air Conditioning Window Unit Cooling Capacity";

# Input, gets the room dimensions and shade information from the user.
roomLength = float(input("Please enter the length of the room (in feet): "))
roomWidth = float(input("Please enter the width of the room (in feet): "))
shadeAmt = int(input("What is the amount of shade that this room receives?"+
                     '\n''\n'
                     "\t1. Little Shade"+'\n''\n'
                     "\t2. Moderate Shade"+'\n''\n'
                     "\t3. Abundant Shade"+'\n''\n'
                     "Please select from the options above: "))

# Process, perform necessary calculations.
roomArea = (roomLength * roomWidth);  # Determine the area of the room.

# Calculates and assigns base BTU requirement based on area before factoring in 
# shade.
if (roomArea < 250):
    btu = 5500;
elif (roomArea <= 500):
    btu = 10000;
elif (roomArea <= 1000):
    btu = 17500;
else:
    btu = 24000;
        
# Assigns appropriate string to menu selection for display later. Also adds or
# reduces btu capacity based on the amount of shade entered by the user.
if (shadeAmt == 1):
    shadeAsString = "Little";
    btu = (btu * 1.15);          # Adds 15% capacity for having little shade.
elif (shadeAmt == 3):
    shadeAsString = "Abundant";
    btu = (btu * 0.9);           # Reduces btu capacity 10% for lots of shade.
else:
    shadeAsString = "Moderate";

# Output, displays calculated information about the room and required BTU's.
print('\n' + CAPACITYHEADING + '\n');
print("Room Area (in square feet): " + format(roomArea) + '\n');
print("Amount of Shade: " + shadeAsString + '\n');
print("BTU's Per Hour needed: " + format(btu, ',.0f'));
