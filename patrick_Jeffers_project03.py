# Patrick Jeffers   Project 3   11/29/2021
# This program takes room dimensions and shade characteristics from the user.  
# This data is then used to calculate the area of the room and the required 
# BTU capacity needed of the rooms air conditioner. Modifications now include 
# the ability to calculate additional rooms, track the number of rooms and input
# validation. Project 3 now modularizes the program.

def main():
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
    
    # Loop to allow for additional rooms.
    while anotherRoom == "Y" or anotherRoom == "y":
    # Input. Gets the room name, dimensions and shade information from the user.
        numRooms += 1            #Accumulator for the number of rooms processed.
        roomName = input("Please enter the name of the room: ")
        roomLength = float(input("Please enter the length of the room"\
                                 "(in feet): "))
        while roomLength < 5:                  #Input validation for roomLength.
            print("Invalid entry. Room length must be larger than 5 feet.")
            roomLength = float(input("Please enter the length of the room" \
                                     " (in feet): "))
        roomWidth = float(input("Please enter the width of the room"\
                                " (in feet): "))
        while roomWidth < 5:                    #Input validation for roomWidth.
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
        while shadeAmt < 1 or shadeAmt > 3:          #Input validation for menu.
            print("Invalid entry. Your selection was not one of the options "\
                  "above.")
            shadeAmt = int(input("\n\nWhat is the amount of shade that this " \
                                 "room receives?"+
                                 '\n''\n'
                                 "\t1. Little Shade"+'\n''\n'
                                 "\t2. Moderate Shade"+'\n''\n'
                                 "\t3. Abundant Shade"+'\n''\n'
                                 "Please select from the options above: "))
        
        # Calculates room area.
        roomArea = calculateArea(roomLength, roomWidth)
        
        # Calculates btu required.
        btu = calculateBTUsPerHour(roomArea, shadeAmt)
        
        # Converts shade to a string for display later.
        shadeAsString = translateShadeChoiceToString(shadeAmt)
        
        # Displays heading.
        displayTitle()
        
        # Displays information about the room, including calculations.
        displayRoomInformation(roomName, roomArea, shadeAsString, btu)
        
        # Determines if there are more rooms to enter.
        anotherRoom = input("Would you like to enter information for another "\
                            "room (Y/N)? ")
        print() #Spacing
    #Final output of the number of rooms processed.
    print("The total number of rooms processed was: " + format(numRooms))

        
# Displays heading.
def displayTitle():
    print()
    print("Air Conditioning Window Unit Cooling Capacity")
    print()
    
# Calculates room area.
def calculateArea(roomLength, roomWidth):
    roomArea = (roomLength * roomWidth)
    return roomArea
    
# Converts shade to a string for display later.
def translateShadeChoiceToString(shadeAmt):
    # Assigns appropriate string to menu selection for display later.
    if (shadeAmt == 1):
        shadeAsString = "Little"
    elif (shadeAmt == 3):
        shadeAsString = "Abundant"
    else:
        shadeAsString = "Moderate"
    return shadeAsString

# Calculates btu required.
def calculateBTUsPerHour(roomArea, shadeAmt):
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
        
    # Adds or reduces btu capacity based on the amount of shade.
    if (shadeAmt == 1):
        btu = (btu * 1.15)          # Adds 15% capacity for having little shade.
    elif (shadeAmt == 3):
        btu = (btu * 0.9)          # Reduces btu capacity 10% for lots of shade.
        
    return btu

# Displays information about the room, including calculations.    
def displayRoomInformation(roomName, roomArea, shadeAsString, btu):
    print("Room Name: " + roomName)
    print("Room Area (in square feet): " + format(roomArea))
    print("Amount of Shade: " + shadeAsString)
    print("BTU's Per Hour needed: " + format(btu, ',.0f') + '\n')

# Calls the main function to run the program.
main()