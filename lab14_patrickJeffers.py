# Patrick Jeffers   Lab14   9/30/2021
# Chapter 5 exercise 23.  This program uses modular code and turtle graphics to 
# draw a snowman.  In addition to the book requirements this program adds 
# buttons and a scarf.

# To use turtle graphics.
import turtle

# The main function, controlling the program.
def main():

    
    # Named constants
    SCREEN_WIDTH = 500    # Screen width
    SCREEN_HEIGHT = 800   # Screen height
    
    # Setup the window size, background color, speed, pen size and starting
    # point. Preparing everything to start drawing.
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.bgcolor("light grey")
    turtle.pensize(2)
    turtle.speed(10)
    turtle.penup()
    turtle.goto(0,-300)
    turtle.pendown()
    
    # Function calls to draw the snowman.  The name of each is what they are
    # responsible for drawing.
    drawBase(100)
    drawMidSection(65)
    drawHead(40)
    drawHat()
    drawArms()
    drawScarf()
    turtle.hideturtle()        # Hides the turtle after all drawing is finished.
    

# Draws the base of the snowman.
def drawBase(size):
    turtle.circle(size)

# Draws the middle section of the snowman.
def drawMidSection(size):
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.goto(0,-65)
    turtle.fillcolor("black")                      # From here to the end of the 
    turtle.begin_fill()                            # funtion draws the buttons.
    turtle.pendown()
    turtle.circle(9)
    turtle.penup()
    turtle.goto(0,-35)
    turtle.pendown()
    turtle.circle(7)
    turtle.penup()
    turtle.goto(0,-10)
    turtle.pendown()
    turtle.circle(5)
    turtle.end_fill()

# Draws both of the arms.
def drawArms():
    turtle.penup()                                          # Snowmans left arm.
    turtle.goto(62,-15)
    turtle.pendown()
    turtle.setheading(15)
    turtle.forward(80)
    turtle.setheading(55)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(25)
    turtle.setheading(-25)
    turtle.forward(25)
    turtle.penup()
    turtle.goto(-62,-15)                                   # Snowmans right arm.
    turtle.pendown()
    turtle.setheading(165)
    turtle.forward(60)
    turtle.setheading(105)
    turtle.forward(40)
    turtle.setheading(165)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(25)
    turtle.setheading(90)
    turtle.forward(25)    

# Draws the head of the snowman, including face.
def drawHead(size):
    turtle.penup()
    turtle.goto(0,30)
    turtle.pendown()    
    turtle.circle(size)
    turtle.penup()
    turtle.goto(-15,75)                                    # Snowmans right eye.
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(15,75)                                      # Snowmans left eye.
    turtle.pendown()
    turtle.circle(5)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-20,60)                                                 # Mouth.
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(40)    
    

# Draws the snowmans hat.
def drawHat():
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()    
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(45)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(60)
    turtle.end_fill()
    
# Draws the snowmans scarf.
def drawScarf():
    turtle.penup()
    turtle.goto(0,28)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()    
    turtle.setheading(0)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(6)
    turtle.left(90)
    turtle.forward(30) 
    turtle.left(90)
    turtle.forward(6)
    turtle.left(90)
    turtle.forward(15)
    turtle.penup()
    turtle.goto(12,28)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(5)
    turtle.goto(0,28)
    turtle.goto(-12,28)
    turtle.pendown()
    turtle.setheading(225)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(5)
    turtle.goto(0,28)
    turtle.end_fill()

# Calling the main function to run the program.
main()
turtle.done()