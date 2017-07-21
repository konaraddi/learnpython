# You've already used some functions
# len(), range(), print(), type(), str(), int()

# More about scoping
def g():
	x=999999
	print(x)

x=0 # This won't matter, the x in the function is different
g()

# Ask students to guess what the last 4 lines will do
def do_something(a,b):
	x=a+b
	y=a-b
	print(x*y)
	return x/y
a=1
b=2
x=5
y=6

print(do_something(x,y))
print(do_something(a,b))
print(do_something(x,a))
print(do_something(y,b))

# Have students guess before they try it out themselves


# NESTING
# Just like how u can nest loops, you can also nest functions

def read_play():
	def read(line):
		print("Alfred: ", line)
	read("Hey")
	read("I'm Alfred")
	read("They don't call me Alfred for nothing")
read_play()

# Have students write a more complex dialogue, between multiple ppl

# functions can be passed in as parameters too
def play_sport(sport):
	print("Let's play a sport")
	sport()

def soccer():
	print("We're playing soccer")

def bball():
	print("We're playing basketball")

play_sport(soccer)
play_sport(bball)

# you can also return a function

def whats_next():
	response=input("Are you hungry? (Y or N)")
	if response == 'Y':
		return eat()
	else:
		print("Alright.")
		return None

def eat():
	print("Eat some noodles")

whats_next()
