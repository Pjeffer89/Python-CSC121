# Patrick Jeffers   Lab07   9/3/2021
# This program was modified per the instructions in chapter 3 exercise 19.
# Modifications include hints to help the user decide whether to use more or
# less angle and force after playing the game and missing the target.

# Hit the Target Game
import turtle

# Named constants
SCREEN_WIDTH = 600    # Screen width
SCREEN_HEIGHT = 600   # Screen height
TARGET_LLEFT_X = 100  # Target's lower-left X
TARGET_LLEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25     # Width of the target
FORCE_FACTOR = 30     # Arbitrary force factor
PROJECTILE_SPEED = 1  # Projectile's animation speed
NORTH = 90            # Angle of north direction
SOUTH = 270           # Angle of south direction
EAST = 0              # Angle of east direction
WEST = 180            # Angle of west direction

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user.
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1-10): "))

# Calculate the distance.
distance = force * FORCE_FACTOR

# Set the heading.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

# Did it hit the target?  If so the user is notified.  If not the user is now 
# given hints for how to get closer to the target based upon where the turtle 
# ends up.  If less or greater than certain coordinate ranges, different and
# appropriate hints are given.
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Target hit!')
elif (turtle.xcor() < TARGET_LLEFT_X):
        if (turtle.ycor() < TARGET_LLEFT_Y):
                print('You missed the target. Try a lesser angle '+\
                'and use more force.')
        elif (turtle.ycor() > (TARGET_LLEFT_Y + TARGET_WIDTH)):
                print('You missed the target. Try a lesser angle '+\
                'and use less force')
        else: 
                print('You missed the target. Try a lesser angle. '+\
                'The force is nearly right!')
elif (turtle.xcor() > (TARGET_LLEFT_X + TARGET_WIDTH)):
        if (turtle.ycor() < TARGET_LLEFT_Y):
                print('You missed the target. Try a greater angle '+\
                'and use more force.')
        elif (turtle.ycor() > (TARGET_LLEFT_Y + TARGET_WIDTH)):
                print('You missed the target. Try a greater angle '+\
                'and use less force.')
        else: 
                print('You missed the target. Try a greater angle. '+\
                'The force is nearly right!')
else:
        if (turtle.ycor() < TARGET_LLEFT_Y):
                print('You missed the target. The angle is very close. '+\
                      'Try using more force.')
        else:
                print('You missed the target. The angle is very close. '+\
                      'Try using less force.')

turtle.done()
