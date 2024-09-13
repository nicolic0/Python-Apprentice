
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

def draw_polygon(sides):

    angle = 360/sides # Calculate angle from number of sides
    
    for i in range(sides):                 # Loop through the number of sides
        tina.forward(50)
        tina.left(angle)                         # Move tina forward by the forward distance
                                      # Turn tina left by the left turn

tina.speed(10)
tina.penup()
tina.left(90)
tina.forward(50)
tina.right(90)
tina.left(90)
tina.forward(30)
tina.right(90)
tina.left(180)
tina.forward(50)
tina.right(180)
tina.pendown()
tina.color("gray")
tina.begin_fill()
draw_polygon(3)  
                      # Draw a square

                           # Move tina to another spot on the screendraw_polygon(4)                        # Draw a pentagon


draw_polygon(4)
tina.end_fill()

draw_polygon(5)
tina.color("black")
draw_polygon(6)

draw_polygon(7)

draw_polygon(8)

draw_polygon(9)

draw_polygon(10)

draw_polygon(11)

draw_polygon(12)

draw_polygon(100)
tina.end_fill()
                                     # Move tina to another sp                       # Draw a hexagon

tina.penup()
tina.forward(30)
tina.right(90)
tina.forward(30)
tina.left(90)
tina.forward(30)
tina.right(180)
tina.forward(60)
tina.right(180)

tina.pendown()
tina.write("oh look a cave")
tina.penup()
tina.right(90)
tina.forward(50)
tina.left(180)


turtle.exitonclick()                     # Close the window when we click on it
