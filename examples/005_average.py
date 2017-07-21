# Let's find the average of two numbers given by the user
num1 = input("Gimme a number: ")
num2 = input("Anotha one: ")

# Don't forget to convert to an integer
num1 = int(num1)
num2 = int(num2)

avg = (num1 + num2) / 2
print("The average of", num1, "and", num2, "is", avg)
