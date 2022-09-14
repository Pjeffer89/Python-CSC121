# Patrick Jeffers   Lab05   8/30/2021
# Based on chapter number 3 exercise 15 in the book, this program takes a 
# specified number of seconds entered by the user and converts it to the 
# appropriate larger units and then displays the conversion.

# Variables, declared and initialized.
secs = 0;
mins = 0;
hrs = 0;
days = 0;
numSec = 0;
output = "";

# Input, gets the number of seconds from the user.
numSeconds = int(input("Please enter the number of seconds: "))


# Process, logic structure to calculate the seconds into larger units while
# leaving the remainder in smaller units. Also builds the appropriate output 
# message based on the size of the number entered.  Will only display and 
# calculate larger units if the number of seconds is high enough.
if numSeconds >= 0 and numSeconds < 60:
    secs = format(numSeconds % 60)
    output = "Seconds: " + secs
elif numSeconds >= 60 and numSeconds < 3600:
    mins = format(numSeconds // 60)
    secs = format(numSeconds % 60)
    output = "Minutes: " + mins + '\n'\
             "Seconds: " + secs
elif numSeconds >= 3600 and numSeconds < 86400:
    hrs = format(numSeconds // 3600)
    mins = format((numSeconds % 3600) // 60)
    secs = format((numSeconds % 3600) % 60)
    output= "Hours: " + hrs + '\n'\
             "Minutes: " + mins + '\n'\
             "Seconds: " + secs
elif numSeconds >= 86400:
    days = format(numSeconds // 86400)
    hrs = format((numSeconds % 86400) // 3600)
    mins = format(((numSeconds % 86400) % 3600) // 60)
    secs = format(((numSeconds % 86400) % 3600) % 60)
    output = "Days: " + days + '\n'\
             "Hours: " + hrs + '\n'\
             "Minutes: " + mins + '\n'\
             "Seconds: " + secs

# Output, displays the processed results.
print(output)