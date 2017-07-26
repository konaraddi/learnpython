# TUPLES
# another object

# Sometimes we want to store items in a list.
# Such as a list of guests invited to a party

# You could just make a string
guest_list = "Alfred Robert John"
# but what if you want to store both the first and last name?
guest_list = "Alfred Borden Robert Angier John Cutter"
# this looks messy, how many guests are coming?
# difficult to extract an item out of this list
# Strings aren't meant for lists


# Introducing, TUPLES! A data type meant exactly for lists
example_tuple=("a", "list" , "of", "words")
example_tuple2=("x", 3, True, None)
# A tuple can hold multiple data types, even at once

# Now we can store our guest list in a tuple
guest_list= ("Alfred Borden", "Robert Angier", "John Cutter")
print(guest_list)

# OPERATIONS ON TUPLES

# Adding tuples together
new_list=("a","b","c")+("x","y","z")
print(new_list)

# Getting an item from a specific index (explain that lists start at 0, not 1)
second_guest= guest_list[1]
print(second_guest)

# Finding the length of a list
num_of_guests= len(guest_list)
print(num_of_guests)

# Using a tuple to swap objects
# suppose you have a couple variables you wanna swap the values
dad="Linda"
mom="Joe"
# you can use a tuple to swap the values of the 'dad' and 'mom' variables
(dad, mom)=(mom, dad)
print("Dad's name:")
print(dad)
print("Mom's name:")
print(mom)


# LISTS
# So far we've made lists with tuples. Python has a second kind of lists, this time called "list"

list_of_numbers=[1,2,3,4,5]
print(type(list_of_numbers))

# What's different about this than a tuple? Here are a few differences:

# You can swap out values in a list
list_of_numbers[0]= 6
print(list_of_numbers)
list_of_numbers[0]= 1
print(list_of_numbers)

# Easier to add to the list
list_of_numbers.append(6)
list_of_numbers.extend([7,8,9]) #adding another list

# Mixed object types are allowd
list_of_numbers.append('ten')
print(list_of_numbers)

# Remove specific items
list_of_numbers.remove('ten')
print(list_of_numbers)

# However, due to this extra functionality, lists take up more space on a computer
