# EXPRESSIONS
# are also Objects

# Expressions contain multiple objects or variables with operators

# Operators:
'''
Add: a + b
Substract: a - b
Multiply: a * b
Divide: a / b
Modulus (finding the remainder): a % b
Power: a ** b
'''

print(2 + 3)

x = 12
print(x - 4)

y = 3
product = x * y
print(product)

z = 72
print(z / 4)

a = 5
b = 3
remainder = 5 % 3 # Here we are assigning an expression '5 % 3' (an object) to the name 'remainder'
print(remainder + y - b)


# You can also use floats

a = 0.7 # Note that I'm updating the variable "a" from before
b = 0.3 # Updating variable "b" from before
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

# Note that computers can't solve equations like 2n + 3 = 12, they can only solve expressions like 4 + 2

# So far we've made expressions with integers (whole numbers) and floats (decimal numbers)
# We can also add strings together

print("Hello" + " World")


my_name = "Omkar"
print("My name is " + my_name)

# We can't add integers or floats with strings (show by example and go over errors here)
# print(3 + "Hello")

# But wait, remember what we said about casting?

# Also, we can multiply a string by an integer
print(3 * "Hello")

# And there's a way to print various types without adding or casting them
print(3, "Hello") # note that spaces are automatically added when printing like this

# Check students grasp concept with stuff like a = a + b

# What does the below print out?
a = 32
b = 64
total = a + b
print(total)
a = -64
print(total)

# How about this?
a = 3
b = 4
c = 5
a = b = c
print("a =", a)
print("b =", b)
print("c =", c)

# Btw you can do this in the console (show students)
