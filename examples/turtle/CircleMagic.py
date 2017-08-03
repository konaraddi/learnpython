import turtle
import random

win = turtle.Screen()

turtle.speed(0)
turtle.colormode(255)
for i in range(200):
    turtle.circle(50)
    turtle.left(i)
    turtle.circle(-50)
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    turtle.color(r,g,b)
    
turtle.exitonclick()
