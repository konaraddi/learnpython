# FILE I/O

# So far we've used predefined variables and data inputted by the user. Now let's use files.

# Make a list of words in a txt file

# How to read from a file

word_file = open('./010_words.txt') # File object
print(type(word_file))

def read(file):
    list = () # create an empty tuple
    for line in file:
            # File contain strings, or sequences of characters, but they also contain a "\n" to represent a new line
            item = line.replace("\n", "")
            list += (item,) # adding an item to a tuple
    return list;

word_list = read(word_file)

# Print each word in the list
for word in word_list:
        print(word)

# Another way to print each word in a list
for i in range(len(word_list)):
        print(word_list[i])
