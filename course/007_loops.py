# LOOPS in Python

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
