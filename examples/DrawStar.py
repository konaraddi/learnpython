import turtle
t = turtle.Pen()
t.color('red')
'''
The trick to this star function is to divide 360 degrees into the
number of points, which gives the interior angle for each point of
the star (see line 'angle = 360/points' in the following code). To determine the exterior
angle, we subtract that number from 180 to get the number of
degrees the turtle must turn at line 't.left(180 - angle)'.

In order to move around
in a circular pattern, drawing the spines, we need to increase the
angle, so we multiply the calculated angle by two and turn the
turtle right at line 't.right(180-(angle * 2))'.

'''
def draw_star(size, points):
    angle = 360 / points
    for x in range(0, points):
        t.forward(size)
        t.left(180 - angle)
        t.forward(size)
        t.right(180-(angle * 2))

draw_star(100, 5)