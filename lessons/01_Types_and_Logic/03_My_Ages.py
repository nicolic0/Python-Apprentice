
"""
Am I Big Yet?

Ask the user's age then use an if-elif-else statement to 
tell the user what age groups the user is in. The groups are:

0-2: Baby
3-5: Toddler
6-12: Child
13-19: Teen
20-64: Adult
65+: Senior

Except, if the user is the same age as you, print "You are pretty awesome!"

Here is how you ask the user's age in integer format.  The first argument is 
the title of the window, the second is the message to the user.

age = simpledialog.askinteger("Your Age", "How old are you?") 

Or, you could ask the user for a float with simpledialog.askfloat() 

age =  simpledialog.askfloat("Your Age", "How old are you?")


Here is how you show the user a message window. The first parameter is the title of the window, 
the second is the message to show the user.

messagebox.showinfo('What you are', "You are a baby.")

"""

from tkinter import messagebox, simpledialog, Tk # import required modules
import turtle
age=simpledialog.askinteger(title="",prompt="what is you age sir")
window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups
# Ask the user's age

# Use if statements to determine dr3the age group
# and create a message

# Show the message to the user

if age > 0 and age < 3:
    print("baby")
if age > 2 and age < 6:
    print ("toddler")
if age > 5 and age < 13:
    print ("child")
if age > 12 and age < 20:
    print("teenager")
if age > 19 and age < 65:
    print ("adult")
if age > 64:
    print ("you old geezer")
if age > 11 and age < 13:
    print ("you are goated")

window.mainloop()  # Keeps the window open


# TODO: 
# Try to write your program so you only need to use one messagebox.showinfo() function.
