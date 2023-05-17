import turtle
import random

# Create a turtle and initialize its variables
sam = turtle.Turtle()
sam.speed(0)
sam.width(5)

# Create a list of colors
colors = ["blue", "red", "green", "orange", "black", "yellow", "purple", "pink"]

# Functions to be called on some event
def up():
    sam.setheading(90)
    sam.forward(100)

def down():
    sam.setheading(270)
    sam.forward(100)
    
def left():
    sam.setheading(180)
    sam.forward(100)
    
def right():
    sam.setheading(0)
    sam.forward(100)

def clickleft(x, y):
    sam.color(random.choice(colors)) # choose a random element from the colors list and set it to the turtle's color

def clickright(x, y):
    sam.stamp() # stamp the shape of the turtle on the screen

# We need to tell the program to listen for a trigger
turtle.listen()

# Define the triggers and which event happens based on which trigger
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.onscreenclick(clickleft, 1) # 1 means left mouse
turtle.onscreenclick(clickright, 3) # 3 means right mouse

# mainloop() always goes last and will keep looping the listeners, always waiting.
# Without this method, the program will quit immediately
turtle.mainloop()
