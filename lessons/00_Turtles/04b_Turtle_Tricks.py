"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


... # Your code here
tina.speed(100)
tina.pensize(10)
tina.penup()
tina.goto(50,90)
tina.pendown()
tina.left(90)
tina.forward(50)
tina.left(90)
tina.forward(50)
tina.left(90)
tina.forward(50)
tina.left(90)
tina.forward(50)
tina.left(180)

tina.penup()
tina.forward(150)
tina.right(90)

tina.pendown()
tina.forward(50)
tina.right(90)
tina.forward(50)
tina.right(90)
tina.forward(50)
tina.right(90)
tina.forward(50)
tina.left(90)

tina.penup()
tina.forward(60)
tina.left(90)

tina.pendown()
tina.forward(160)

tina.penup()
tina.left(90)
tina.forward(140)
tina.left(90)

tina.begin_fill()
tina.color("blue")
tina.pendown()
tina.forward(160)
tina.right(180)
tina.forward(30)
tina.left(90)
tina.forward(60)
tina.right(90)
tina.forward(100)
tina.right(90)
tina.forward(60)
tina.left(90)
tina.forward(30)
tina.end_fill()

tina.penup()
tina.left(270)
tina.forward(160)
tina.right(90)
tina.forward(50)
tina.right(90)
tina.forward(20)
tina.right(180)

tina.begin_fill()
tina.pendown()
tina.color("red")
tina.forward(60)
tina.right(90)
tina.forward(30)
tina.right(90)
tina.forward(60)
tina.right(90)
tina.forward(30)
tina.end_fill()
turtle.exitonclick()                    # Close the window when we click on it
