#Import everything from Turtle package, which contains drawing functions
#We will be using the functions from thisTurtle package to do some fun with drawing
from turtle import *

#We will define a function which will parse the commands to draw
# F => Forward; B => Backward and so.....
# First will change everything to UPPER case using upper() function
def turtle_controller(do, val):
    do = do.upper()
    if do == 'F':
        forward(val)
    elif do == 'B':
        backward(val)
    elif do == 'R':
        right(val)
    elif do == 'L':
        left(val)
    elif do == 'U':
        penup()
    elif do == 'D':
        pendown()
    elif do == 'N':
        reset()
    else:
        print('unknown command')

# Test he above function with belwom calls
#turtle_controller('F', 100)
#turtle_controller('R', 90)
#turtle_controller('F', 100)

#STEP 2

def string_artist(program):
    #split the input using '-' as our separator
    #each item between '-' will be an individual item added to list
    cmd_list = program.split('-')
    #For each item in list run some processing with the FOR loop
    for command in cmd_list:
        #Get the length of the current item, which we call as command here
        cmd_len = len(command)
        #if the length is ZERO continue and get next item
        if cmd_len == 0:
            continue
        #Get the first character from command item. ZERO based list. ZERO is first item
        cmd_type = command[0]
        #initialize num to zero. each loop run needs to reset, otherwise the value will carry over
        num=0
        if cmd_len > 1:
            #When length is greater than 1, get the remaining charaters
            num_string = command[1:]
            #convert the remaining into integer
            num=int(num_string)
        #print the final command and the separated command and value
        print(command, ':', cmd_type, num)
        #Now call the drawing function
        turtle_controller(cmd_type, num)

# Test by calling the below function with a string of command in it
#string_artist('N-L90-f100-r45-f70-r90-f70-r45-f100-r90-f100')

#STEP 3
# Create a GUI window
# Every between TRIPLE ' is printed as it is, including the NEW LINE
instructions = '''Enter a program for turtle:
eg: F100-R45-U-F100-L45-D-F100-R90-B50
N = New drawing
U/D = Pen Up/Down
F100 = Forward 100
B50 = backward 50
R90 = Right turn 90 deg
L45 = Left turn 45 deg'''

#This creates the screen for drawing
screen = getscreen()
while True:
    # This creates a window and the window will have an INPUT BOX and the title and the aboe BIG instruction will be used as label for input box
    t_program = screen.textinput('drawing Machine', instructions)
    #printing thie creates the window
    print(t_program )
    #If there is nothing or user presses CANCEL or END is typed then it will end the program
    if (t_program == None or t_program.upper()=='END'):
        break
    #Send the user input to our drawinf artist function
    string_artist(t_program)