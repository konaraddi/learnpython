# MAKING GRAPHICAL USER INTERFACES WITH TKINTER

#import everthing from tkinter, a Python module for making GUIs
'''
from tkinter import *

# Create the window
window = Tk()

# Create the text, specifying it to be on the window and the text to show
text = Label(window, text="Hello World!")
text.pack() # Makes the text visible

window.mainloop() # Makes the window and everything else on the window visible
'''

# Making a button add text, resizing window
'''
from tkinter import *

window = Tk()

def addtext():
    newtext= Label(window, text="Hi, I just got here")
    newtext.pack()

button = Button(window, text="Click me!", command=addtext)
button.pack()

window.minsize(300,200)
window.mainloop()
'''

# Updating a label using a button and setting the minimum dimensions of a window
from tkinter import *

window = Tk()

label_text= StringVar()
label= Label(window, textvariable=label_text)
label.pack()
label_text.set("Hello")

changes_made = 0
def changelabel():
    # Use global to edit variables made outside of a function
    global label_text
    global changes_made

    changes_made += 1 # We are editting a variable defined outside this function
    label_text.set("Hello " + " again" + " and again" * changes_made)

# Make a button, set the text, and set the function when clicked
button = Button(window, text="Let's change the text above!", command=changelabel)
button.pack()

# Close button
button = Button(window, text="Close", command=window.destroy)
button.pack()

# Set minimum size of window (Width, Height)
window.minsize(300,200)

window.mainloop()
