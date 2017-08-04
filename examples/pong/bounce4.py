# The ball should bounce between the top and bottom edges when run
from tkinter import *
import random
import time

# Created a window
tk = Tk()

# Adding a title to our window
tk.title("Game")

# The window is a fixed size, it cannot be changed
tk.resizable(0, 0)

# Places the window on top of our other windows
tk.wm_attributes("-topmost", 1)

# Creates the canvas for our game
# Passing in parameters: window, dimensions, no border
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)

# Setting the canvas size to the dimensions above
canvas.pack()

# Creates the window with our canvas
tk.update()

# Let's make our ball
class Ball:

    # A function that "initializes" the ball; it creates the ball
    def __init__(self, canvas, color):
        # Making the bckgrnd the canvas
        self.canvas = canvas
        # Creates the shape and color of the ball
        # (10,10) are the x,y coords for the top-left of the ball
        # (25,25) are the x,y coords for the bot-right of the ball
        # Our ball is 15 x 15
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        # Move the ball to the middle of the canvas: (245,100)
        self.canvas.move(self.id, 245, 100)
        # Setting the ball's initial movement with x & y
        self.x = 0
        self.y = -1
        # We do this so the ball can "remember" the height of the canvas
        self.canvas_height = self.canvas.winfo_height()
    
    # We've come back to this again
    def draw(self):
        # These lines below will make the ball bounce when it reaches the edges
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1

# Create the ball, you can change the color        
ball = Ball(canvas, 'red')

# Tells tkinter, our window, to update every 1/100 second forver
# (or at least until we close the window)
while 1:
    # redraw the ball
    ball.draw() # Now, when you run the game, the ball should move up
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

