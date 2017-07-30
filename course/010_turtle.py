# TURTLE

import turtle
# Here we are "including" a module called "turtle"

window = turtle.Screen()

# "Bucky" is the name of my turtle, name your turtle whatever you like
bucky = turtle.Turtle()

'''
bucky.forward(100)
bucky.right(90)
bucky.forward(100)
bucky.right(90)
bucky.forward(100)
bucky.right(90)
bucky.forward(100)
bucky.right(90)
'''

'''
# Wait a minute, let's use a loop
for x in range(4):
    bucky.forward(100)
    bucky.right(90)
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
