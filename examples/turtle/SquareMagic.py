import random
import turtle

win = turtle.Screen()

def square(size):
    for i in range(0,4):
        turtle.forward(size)
        turtle.left(90)

def octagon(size):
    #Start from 1 and end at 9. 9-1=8 => 8 sides of an octagon.
    #This loop will draw eight sides
    for x in range(1,9):
        #Draw each side with given size
        turtle.forward(size)
        #the outer angle is 45 deg. That means inner angle is 135 deg each
        turtle.right(45)

turtle.speed(0)
turtle.colormode(255)
for i in range(180):
    octagon(120)
    square(120)
    square(200)
    turtle.circle(30)
    turtle.left(2*i)
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    turtle.color(r,g,b)
 
turtle.exitonclick()