# Patrick Jeffers   Lab10   9/22/2021
# Chapter 4 exercise 17.  This program uses a loop with turtle graphics to draw
# a particular star pattern.  The loop allows for much less code than it would
# take otherwise.

# Star Pattern.
import turtle

# Named constants
SCREEN_WIDTH = 800    # Screen width
SCREEN_HEIGHT = 800   # Screen height

# Setup the window size.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Positions the turtle so that it is more centered in the window.
turtle.penup()
turtle.goto(-150,100)
turtle.pendown()

# Loop to draw the star pattern.
for x in range (8):
    turtle.forward(300)
    turtle.right(135)
    
# Hides turtle from view of star pattern.
turtle.hideturtle()

turtle.done()