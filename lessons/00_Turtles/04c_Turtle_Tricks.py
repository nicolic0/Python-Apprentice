"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.

"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes


... # Your code here
tina.speed(10)
tina.hideturtle()
tina.penup()
tina.left(90)
tina.forward(200)
tina.left(90)
tina.forward(270)
tina.right(180)

tina.showturtle()
tina.forward(210)
tina.write("i can go invisable like a ghost!")
tina.forward(100)
tina.right(90)
tina.forward(60)
tina.right(90)
tina.write("watch this")
tina.forward(50)
tina.right(90)
tina.hideturtle()
tina.right(180)
tina.forward(90)
tina.showturtle()
tina.right(90)
tina.forward (90)
tina.right(180)
tina.write("i teleported")
tina.hideturtle()
tina.forward(50)
tina.left(90)
tina.forward(120)
tina.showturtle()
tina.right(90)
tina.write("OVER HERE")
tina.hideturtle()
tina.right(180)
tina.forward(60)
tina.left(90)
tina.forward(70)
tina.showturtle()
tina.write("OVER HERE")
tina.hideturtle()
tina.right(180)
tina.forward(130)
tina.left(90)
tina.forward(90)
tina.showturtle()
tina.write("OVER HERE")
tina.hideturtle()
tina.left(90)
tina.forward(250)
tina.left(90)
tina.forward(120)
tina.write("OVER HERE")





turtle.exitonclick()                    # Close the window when we click on it


# Dont forget to check in your code!