# TURTLE

import turtle
# Here we are "including" a module called "turtle"

window = turtle.Screen()

# "Bucky" is the name of my turtle, name your turtle whatever you like
bucky = turtle.Pen()

# You can define more than one turtle
alfred = turtle.Pen()

import time
time.sleep(3)

# Functions for Bucky:
'''
 .forward(int), 
 .backward(int), 
 .right(int), 
 .left(int), 
 '''
# You can use negative numbers too!
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

.circle(int)

for the below, int = hex, rgb, or a word like "red"
.color(int) -> pen color
.color(int, int) -> pen color & fill color
'''



