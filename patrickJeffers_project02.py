# Patrick Jeffers   Project 2   10/24/2021
# This program takes room dimensions and shade characteristics from the user.  
# This data is then used to calculate the area of the room and the required 
# BTU capacity needed of the rooms air conditioner. Modifications now include 
# the ability to calculate additional rooms, track the number of rooms and input
# validation.

# Variables, (all lengths are in feet / area in sqft.)
roomLength = 0.0
roomWidth = 0.0
roomArea = 0.0
shadeAmt = 0
btu = 0.0
numRooms = 0
shadeAsString = ""
roomName = ""
anotherRoom = "Y"


# Constants
CAPACITYHEADING = "Air Conditioning Window Unit Cooling Capacity"

# Loop to allow for additional rooms.
while anotherRoom == "Y" or anotherRoom == "y":
    # Input. Gets the room name, dimensions and shade information from the user.
    numRooms += 1                #Accumulator for the number of rooms processed.
    roomName = input("Please enter the name of the room: ")
    roomLength = float(input("Please enter the length of the room (in feet): "))
    while roomLength < 5:                      #Input validation for roomLength.
        print("Invalid entry. Room length must be larger than 5 feet.")
        roomLength = float(input("Please enter the length of the room" \
                                 "(in feet): "))
    roomWidth = float(input("Please enter the width of the room (in feet): "))
    while roomWidth < 5:                        #Input validation for roomWidth.
        print("Invalid entry. Room width must be larger than 5 feet.")
        roomWidth = float(input("Please enter the width of the room" \
                                "(in feet): "))
    shadeAmt = int(input("\n\nWhat is the amount of shade that this room " \
                         "receives?"+
                         '\n''\n'
                         "\t1. Little Shade"+'\n''\n'
                         "\t2. Moderate Shade"+'\n''\n'
                         "\t3. Abundant Shade"+'\n''\n'
                         "Please select from the options above: "))
    while shadeAmt < 1 or shadeAmt > 3:              #Input validation for menu.
        print("Invalid entry. Your selection was not one of the options above.")
        shadeAmt = int(input("\n\nWhat is the amount of shade that this room " \
                             "receives?"+
                             '\n''\n'
                             "\t1. Little Shade"+'\n''\n'
                             "\t2. Moderate Shade"+'\n''\n'
                             "\t3. Abundant Shade"+'\n''\n'
                             "Please select from the options above: "))        

    # Process, perform necessary calculations.
    roomArea = (roomLength * roomWidth)        # Determine the area of the room.

    # Calculates and assigns base BTU requirement based on area before factoring
    # in shade.
    if (roomArea < 250):
        btu = 5500
    elif (roomArea <= 500):
        btu = 10000
    elif (roomArea <= 1000):
        btu = 17500
    else:
        btu = 24000
        
    # Assigns appropriate string to menu selection for display later. Also adds
    # or reduces btu capacity based on the amount of shade entered by the user.
    if (shadeAmt == 1):
        shadeAsString = "Little"
        btu = (btu * 1.15)          # Adds 15% capacity for having little shade.
    elif (shadeAmt == 3):
        shadeAsString = "Abundant"
        btu = (btu * 0.9)          # Reduces btu capacity 10% for lots of shade.
    else:
        shadeAsString = "Moderate"

    # Output, displays calculated information about the room and required BTU's.
    print('\n' + CAPACITYHEADING + '\n')
    print("Room Name: " + roomName)
    print("Room Area (in square feet): " + format(roomArea))
    print("Amount of Shade: " + shadeAsString)
    print("BTU's Per Hour needed: " + format(btu, ',.0f') + '\n')
    anotherRoom = input("Would you like to enter information for another room "\
                        "(Y/N)? ")
    print("")    #Spacing then displays the number of rooms processed when done.
print("The total number of rooms processed was: " + format(numRooms))