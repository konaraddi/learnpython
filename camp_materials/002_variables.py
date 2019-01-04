# VARIABLES

# VARIABLE = object given a name
# A variable has a name and a value (an object)
# The name must start with a letter or underscore, and can contain numbers, letters, or underscore
# How do we assign a variable? Using the '=' sign
x = 1
# In math, the equal sign indicates an equality. In programming, it indicates that we are setting something equal to another.
print(x) # what if we do print("x")?

# Variables also have types:

# INTEGERS (int type)
# Whole numbers.
a = 3
b = -4
age = 72
print(a, b, age)
a,b,c=1,2,3

# FLOATS (float type)
# Decimal numbers
x = 0.2
y = 3.0
weight = 132.3
print( x, y , weight)

# BOOLEANS (bool type)
# True or False
summer = True
winter = False
print(summer, winter)

# STRINGS (str type)
# Series of characters (letters, numbers, punctuation, etc.)
greeting = "Hey Bob! How's it going?"
car = "2017 Porsche 911 Carrera"
pet = "Alfred the Dog"
# Making a multiline string
multiple_lines = '''
This is on
multiple
lines.
'''
print(multiple_lines)

# Use "\" as an escape sequence
print("Bob said, \"I'm hungry!\"")

#Use \n to make a new line
print("This is one line \n And this is one another")

# You can find the length of a string using len()
word = "dictionary"
length = len(word)
print(length)

# NO VALUE (NoneType type)
# "None" is the "null" in Python
nothing = None
tokens = None
print(nothing)

# You can check the type of a variable w/ type()

# You can change certain types of variables to other types (i.e. "casting")
# int(), float(), bool(), str()
