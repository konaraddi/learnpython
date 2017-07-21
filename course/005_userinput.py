# User INPUT

# How do we get a input from the user?
input()

# For example, you can ask the user what's their name
input("What is your name? ")
# We add a space after the question so there's a space in between the
# prompt and user's answer/input.
# Alternatively, we can use '\n' for a new line
input("What is your name?\n")

# But what good is asking for input without storing the input?
user_name= input("What is your name?\n")
# The line below is executed as soon as user input is received
print("Oh yeah, I remember now, your name is", user_name)

# Anything the user types in will be a string
# But we can convert it to an int
age = input("How old are you?\n")
age = int(age) #casting
print("You have", 18 - age, "years until you're an adult!")

# EXERCISES

# 1. Ask the user for their first, middle, and last name. Then print their full name.
# 2. Ask the user for 2 numbers, then print the average. 
# 3. Ask the user for their pet name and various stats (e.g. how much HP? Attack/Defense?)
#    then print it all out for the user in a neat fashion.
