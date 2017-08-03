import turtle
t = turtle.Pen()

# Function to draw octagon. It takes size as input parameter
# and also whether to fill the inside of the octagon or not
# 
def octagon(size, filled):
    #If the input parameter for 'filled' is True then mark that in the begining before starting to draw
    if filled == True:
        t.begin_fill()
    
    #Start from 1 and end at 9. 9-1=8 => 8 sides of an octagon.
    #This loop will draw eight sides
    for x in range(1,9):
        t.forward(size)
        t.right(45)
    #When the drawinf is done, make sure to call the END of fill 
    if filled == True:
        t.end_fill()

# Now call our function and test it
octagon(100, True)
