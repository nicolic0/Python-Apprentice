"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""
import random

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)
   # Set the size of the window

baseSize= 200
flameSize= 130

tina = turtle.Turtle()                  # Create a turtle named tina
circle = 60

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)
tina.begin_fill()
tina.forward(64) 

tina.left(40) 

tina.forward(flameSize) 

tina.right(170) 

tina.forward(flameSize) 
    
tina.right(62) 

tina.forward(baseSize) 

tina.end_fill()

tina.hideturtle() 


tina.pendown()

                # Make the turtle move as fast, but not too fast. 


colors = ["red", "blue", "green", "pink", "yellow"] # define a list of colors

for color in range(150):
    tina.color(random.choice(colors))
    tina.fillcolor(random.choice(colors))
    tina.speed(0)
    tina.begin_fill()
    tina.forward(64) 

    tina.left(40) 

    tina.forward(flameSize) 

    tina.right(170) 

    tina.forward(flameSize) 
        
    tina.right(62) 

    tina.forward(baseSize) 

    tina.end_fill()

    tina.hideturtle() 


    tina.pendown()
    if color %10==0:
        flameSize+=5 

                                   # loop through the colors
     # Your code here


# 2) Make another square, but put the colors in reverse order, using a negative index. 

... # Your code here


turtle.exitonclick()                     # Close the window when we click on it