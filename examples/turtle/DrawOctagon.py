import turtle
t = turtle.Pen()

# Function to draw octagon. It takes size as input parameter
def octagon(size):
    #Start from 1 and end at 9. 9-1=8 => 8 sides of an octagon.
    #This loop will draw eight sides
    for x in range(1,9):
        #Draw each side with given size
        t.forward(size)
        #the outer angle is 45 deg. That means inner angle is 135 deg each
        t.right(45)

#Now call our function and test it
octagon(50)