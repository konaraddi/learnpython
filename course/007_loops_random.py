# LOOPS in Python
'''
# FOR loop
print("Starting from 0 and stopping before 4:")
for i in range(4):
	print("the variable i =", i)
# range(end)

# You can specify the starting, ending, and/or steps to take, using range()

print("Starting from 1 and stopping before 5:")
for x in range(1,5):
	print("the variable x =", x)
#range(start, end)

print("Starting from 0, stopping before 8, but every 2 steps:")
for n in range(0, 8, 2):
	print("the variable n=", n)
# range(start, end, step)


# Iterating over a string
word=input("I can spell any word you tell me: ")
for char in word:
	print(char)

# Iterating over a string...backwards!
word=input("Give me a word: ")
for c in range(len(word)-1, -1, -1):
	print(word[c])

# Exercise
# 1. Can you write a program that counts the number of vowels in a word given by the user?
# 2. Ask the user for two numbers. Count how many numbers divisible by 7 are between them.

# Up until now, we knew how many times we needed to repeat a task
# But what if we don't know how many times a task should be repeated?

# Introducing a WHILE loop
# A guessing game, where we don't how many guesses the user will need
secret_num = 12
guess = input("Can you guess what number I'm thinking of?\n")
guess = int(guess)
while guess != secret_num:
	print("Nope, that's not it.")
	guess = input("Try again: ")
	guess = int(guess)
print("Eyyy, you got it!") # We only get here when the while loop ends

# Exercise
# Now I want you to make a game that does exactly that but tells if you're
# getting hotter or colder.

# It's possible to make infinite loops
while True:
	print("The end is near") # the end is not near, it never ends!
# Click the red square button in the top right hand corner to stop the loop


# You can also break out of loops with the keyword 'break'
guess = input("Guess the word I'm thinking of: ")
attempts_left = 3
while guess != 'word':
	attempts_left -= 1
	if attempts_left == 0:
		print("You ran out of tries :(")
		break;
	guess = input("Nope, guess again: ")
if guess == 'word':
	print("Yup! That's correct")

# You can skip the rest of the lines in a loop by using the keyword 'continue'
for x in range (100):
	print(x)
	continue
	print("This message will never be printed.")
'''


# RANDOM
'''
Somtimes we want to pick something randomly, like a random food or number.
'''
import random
# We're "including" a module called "random". This gives us an extra set of tools for generating random objects.

# Assigning a variable a random number from 0 to 5 (including 0 & 5)
random_number= random.randint(0, 5)
# The number isn't chosen until we run the program
# So we have no way to knowing what the number is until we print the variable's value
print(random_number) # This won't necessarily be the same every time

# Generating a random number can help us choose a random item from a list
list_of_items = ["item0", "item1", "item2", "item3", "item4"]
random_index = random.randint(0, len(list_of_items) - 1) # Why do need to subtract 1? Because indices start with 0
random_item = list_of_items[random_index]
print(random_item)

# Or you could just do this
print(random.choice(list_of_items)) # BUT this only works for lists!
