# TURTLE

import turtle
# Here we are "including" a module called "turtle"

window = turtle.Screen()

# "Bucky" is the name of my turtle, name your turtle whatever you like
bucky = turtle.Pen()

import time
time.sleep(3)

# Functions for Bucky: .forward(int), .backward(int), .right(int), .left(int), .circle(int), .color(name)
bucky.forward(100)
bucky.left(90) # degrees
bucky.backward(100)
bucky.right(90) # degrees
bucky.color('blue')
bucky.circle(100)

window.mainloop() # to keep the window open

'''
More functions for Turtle:
.speed(int)

.penup()
.pendown()
.pensize(int)

.file(boolean)

'''


'''
bucky.forward(100)
bucky.right(90)
bucky.forward(100)
bucky.right(90)
bucky.forward(100)
bucky.right(90)
bucky.forward(100)
bucky.right(90)
window.mainloop() # We need this to keep the window open
'''

'''
# Wait a minute, let's use a loop
for x in range(4):
    bucky.forward(100)
    bucky.left(90)
'''

'''
# We just made a square, let's make a function for making a square
def bucky_square():
    # Wait a minute, let's use a loop
    for x in range(4):
        bucky.forward(100)
        bucky.right(90)

bucky_square()
bucky.forward(50)
bucky_square()

window.mainloop()
'''

'''
# We can define multiple turtles
alfred = turtle.Pen()

bucky.forward(100)
alfred.backward(100)

window.mainloop()
'''

