# HANGMAN

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
button = Button(window, text="Update the hang", command=changelabel)
button.pack()

# Close button
button = Button(window, text="Close", command=window.destroy)
button.pack()

# Set minimum size of window (Width, Height)
window.minsize(300,200)

window.mainloop()
