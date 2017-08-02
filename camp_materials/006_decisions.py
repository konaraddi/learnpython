# Making DECISIONS

'''
Discuss booleans (True and False) 
and logical operators: ==, !=, >, <, >=, <= 

Example: 
a = 2
b = 3
print(a > b)
'''

# So far we've made linear programs; they execute line after line in order
# without there being any sort of decision making involved.

# IF statements
'''
if [some condition goes here]:
	[then do something here]
'''

# Note the colon and ident
if 3 > 0:
	print("True, 3 is greater than 0.") # This belongs to the if statement
print("This message is always printed.") # This comes after the if statement


# Example
# The == & !=
fav_num = input("What's your favorite number?\n")
fav_num = int(fav_num)
if fav_num % 2 == 0:
	print("Your favorite number is an even number.")
if fav_num % 2 != 0:
	print("Your favorite number is an odd number.")

# You also use == and != with strings
word = "hello"
if word == "hello":
	print("The word says 'hello'. ")

# If statements can also be nested, as long as you maintain indentation
number = 4
if number > 0:
	print(number, "is positive")
	if number < 5:
		print(number, "is less than 5")

# AND / OR
num1= int(input("Give me a number.\n"))
num2= int(input("Give me anotha' one.\n"))
if num1 > 0 and num2 > 0:
	print("Both numbers you gave me are positive!")
if num1 < 0 or num2 < 0:
	print("At least one of those numbers is negative")

# else if, else
num = int(input("Give me a number: \n"))
# if one of the below is true, then the rest is ignored
if num > 0:
	print(num, "is positive")
elif num < 0:
	print(num, "is negative")
else:
	print(num, "is zero so it's neither positive nor negative")
