# FUNCTIONS

def greet_you():
	your_name=input("What's your name? ")
	print("Hello " + your_name)
	print("My name is Butter")
'''
greet_you()

def greet_you_again(name):
	print("Hello "+ name)

greet_you_again(input("What's your name? "))

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

# Talk about scopes of parameters and variables
# Functions have access to variables in the main program
# The main program can not access variables defined in the function

