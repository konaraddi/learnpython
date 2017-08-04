# Nothing should happen when run
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