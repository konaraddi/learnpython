# FUNCTIONS

'''
Provide example of complicated program ppl use everyday.
Explain that it's made up of multiple modules of code, breaking a big problem into smaller problems,
each with its own purpose to fulfill a certain task. And once you've made a module for a specific task,
it's easy to use it again and again in different places.

In Python, these modules that complete subtasks are called functions.
'''

def greet_you():
	your_name=input("What's your name? ")
	print("Hello " + your_name)
	print("My name is Butter")
'''
greet_you()

# Functions need to be called
# Explain what happens when a function is called

def greet_you_again(name): # These input parameters are not actual variables, they are placeholders
	print("Hello "+ name)

greet_you_again(input("What's your name? "))

# Parameters vs Arguments

def combine_words(word1, word2):
	return word1 + word2

print(combine_words('rain','bow'))

def combine_numbers(num1, num2):
	return num1 + num2

print(combine_numbers(1,2))

# Wait, what's the difference between the last two functions?
'''
# Solve for x in ax+b=c
def solve_for_x(a,b,c):
	return (c-b)/a

# 2x+3=10
print("If 2x+3=10, then x=", solve_for_x(2, 3, 10))

# Oh what if it's 3x-5=12?
x= solve_for_x(3,-5,12) # function called is replaced by what's returned by it
print("If 3x-5=12, then x=", x)

# Note that functions without a return statement are, by default, returning None (the NoneType data)
print(greet_you())
print(type(greet_you()))

# It's important to write comment for functions
def get_years_alive(tree_rings):
	'''
	tree_rings, integer
	Calculates how many years a tree has been alive for.
	Returns an integer, representing the number of years.
	'''
	return tree_rings*1.2

# Talk about SCOPES of parameters and variables

L = 4
def printL():
		print(L)

# Compare the above and below when discussing scopes

def printQ():
		q = 12
		print(q)
print(q)

# Functions have access to variables defined in the main program
# The main program can not access variables defined in the function
