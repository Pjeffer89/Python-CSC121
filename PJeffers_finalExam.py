# Patrick Jeffers   Final Exam   12/9/2021
# The program was created for an online song distribution company. The program
# accepts an order of playlists that allows the user to pick the platform and 
# the number of songs in the playlist. The program will calculate the total of
# the order of playlists while validating user input.

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    # Variables and Global Constants.
    SPOTTYCOSTS = [2.25, 4.50, 6.75]
    MANGOCOSTS = [3.55, 5.75, 9.95]    
    totalCost = 0    
    
    # Main program structure.
    numberOfPlaylists = getPlaylists()
    for i in range(numberOfPlaylists):                 # Loop for each playlist.
        curPlaylistNumber = (i + 1)
        platform = getPlatform(curPlaylistNumber)
        if (platform == 3):    # Ends program per request while still giving the
            print("\nProgram ended.")   # total of the playlists entered so far.
            break
        playlistLength = getPlaylistLength(curPlaylistNumber)
        playlistCost = calculatePlaylistCost(platform, playlistLength, \
                                             SPOTTYCOSTS, MANGOCOSTS)
        totalCost += playlistCost              # Accumulator for the total cost.
    # Outputs the final total.
    print("\nThe total of all playlists: $" + format(totalCost, ',.2f'))


# This function gets the number of playlists from the user while validating the
# users input for a logical entry of at least one.
def getPlaylists():
    numberOfPlaylists = int(input("Enter the number of playlists (min: 1): "))
    while numberOfPlaylists < 1:
        print("\n** ERROR: INVALID NUMBER OF PLAYLISTS **\n")
        numberOfPlaylists = int(input("Enter the number of playlists: "))
    return numberOfPlaylists

# This function gets the platform selection from the user while validating the 
# users input for a valid entry from the menu.  
def getPlatform(curPlaylistNumber):
    print("\nSelect from one of the following streaming platforms:")
    print("\n\t1. Spotty Fire\n\t2. Mango Music\n\n\t3. Quit Program\n")
    platform = int(input("Please choose the streaming platform for "\
                         "playlist #" + format(curPlaylistNumber) + ": "))
    while platform < 1 or platform > 3:
        print("\n** ERROR: INVALID STREAMING PLATFORM **")
        print("\nSelect from one of the following streaming platforms:")
        print("\n\t1. Spotty Fire\n\t2. Mango Music\n\n\t3. Quit Program\n")        
        platform = int(input("Please choose the streaming platform for "\
                             "playlist #" + format(curPlaylistNumber) + ": ")) 
    return platform

# This function gets the length of the playlist from the user while validating
# the users input for a valid entry from the menu.
def getPlaylistLength(curPlaylistNumber):
    print("\nSelect from one of the following playlist lengths:")
    print("\n\t1. Three Songs\n\t2. Five Songs\n\t3. Ten Songs\n")
    playlistLength = int(input("Please choose the length of "\
                         "playlist #" + format(curPlaylistNumber) + ": "))
    while playlistLength < 1 or playlistLength > 3:
        print("\n** ERROR: INVALID PLAYLIST LENGTH **")
        print("\nSelect from one of the following playlist lengths:")
        print("\n\t1. Three Songs\n\t2. Five Songs\n\t3. Ten Songs\n")
        playlistLength = int(input("Please choose the length of "\
                             "playlist #" + format(curPlaylistNumber) + ": "))
    return playlistLength
        
# This function calculates the cost of a playlist using user entered platform
# and playlist length information. This will later be accumulated to come up
# with the final cost.
def calculatePlaylistCost(platform, playlistLength, SPOTTYCOSTS, MANGOCOSTS):    
    if platform == 1:
        if (playlistLength == 1):
            playlistCost = SPOTTYCOSTS[0]
        elif (playlistLength == 2):
            playlistCost = SPOTTYCOSTS[1]
        else:
            playlistCost = SPOTTYCOSTS[2]
    if platform == 2:
        if (playlistLength == 1):
            playlistCost = MANGOCOSTS[0]
        elif (playlistLength == 2):
            playlistCost = MANGOCOSTS[1]
        else:
            playlistCost = MANGOCOSTS[2]
    return playlistCost

# Calls the main function to run the program.        
main()