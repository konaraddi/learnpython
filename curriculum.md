# Learn Python in 15 hours
A 15-hour Python course designed for elementary school kids, developed by Omkar Konaraddi.

Note that this is meant to serve as a guideline that an instructor should follow. This file should not be considered the course itself. This file should not be considered a simple, slim introduction to Python and not wholesome. This file intentionally leaves out certain topics, exceptions, details, etc.

### Day 1
------

`01helloworld.py`


### 2. Getting Started with Python

What's a text editor and IDE?

Walk thru text editor or IDE's functions

New, Saving (* .py), Closing/Opening files

How to make a comment and why you should make comments when you code

"Hello World!" program
```Python
>>> print("Hello World!")
Hello World!
```

Using print() vs not using it (i.e. typing straight into the console)
    * user can see the former, developer can see latter too

### 3. Expressions, Objects, and Variables

Computers can't solve equations like `3 + x = 2` but then can solve expressions like `3 - 2`.

**object**: in Python, an object is any "thing" in Python that can be named. Objects are named so you don't have to refer to them by their description. Much like how you may refer to your pet dog by saying "Alfred", as opposed to saying "you quadrupedal with an acute sense of smell".

Objects have a *type* and *properties*. For example, Alfred is a type of Dog. Some of Alfred's properties may include it's behavior such as barking or his brown hair color.

You can assign expressions and variables (both are objects) a name.

Computer can do math you tell it to by giving it an **expression** "+-/*%"
```Python
>>> 2*3
6

>>> 5-4*2
-3
```

Python can concatenate strings too.
Define a string for students
```
>>> "Hi, " + "I\'m Omkar"
"Hi, I'm Omkar"
```

You can store a certain value (an object), such as the number 12, in something called a **variable**. A variable is a name that has been assigned a value (string or number). For example, `my_favorite_num= 12`.

So, in Python, how do we assign a value to a variable?
What does the "=" means in math vs programming
* "=" states an equality in math
* "=" assigns a value (on the right hand side) to the variable (on the left hand side) in programming

An **object** name must start with a letter or underscore. It can only contain letters, numbers, and strings. There can no be spaces.

```Python
>>> a = 3
>>> b = 2
>>> a + b
5
```
What if one of the variables is a string?
```Python
>>> a = 3
>>> b = "this is a string"
>>> a + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a = "3"
>>> a + b
"3this is a string"
```

You can also set variables to expressions
```Python
>>> a=3
>>> b=2
>>> c=a+b
>>> c
5
```

Can you guess the final value of c below?
```Python
>>> a=3
>>> b=2
>>> c=a+b
>>> print(c)
5
>>> a=7
>>>print(c) #What's the value of the variable "c" now?
```

The value of c is the sum of a and b. When we set `c=a+b`, the computer remembers the value of `c` as 5, not as `a+b` anymore. So the final of value of `c` is still `5`.
```Python
>>> print(c)
5

```

But you can reassign the value of a variable.
```Python
>>> c=12
>>> print(c)
12
```

Is the below accepted by Python?
```Python
>>> 6 - x =2
```
Nope.

How about this?
```Python
>>> a = 3
>>> b = 4
>>> c = 5
>>> a = b = c
```
Yes, now all 3 variables equal 5.

### 4. Object Types and Statements of Code (change title)

Each object has actions or behaviors. Much like how Alfred can bark or pant.

Objects have a type and operations.

### Common Errors and How to debug them

Stuff in Day_1/basics/

### Dividing up Tasks

Provide example of complicated program ppl use everyday.
Explain that it's made up of multiple modules of code, breaking a big problem into smaller problems,
each with its own purpose to fulfill a certain task. And once you've made a module for a specific task,
it's easy to use it again and again in different places.

In Python, these modules that complete subtasks are called functions.
Functions can have input or none at all.
*Parameters vs Arguments*

`functions.py`

Functions need to be called
Explain what happens when a function is called

### Misc

Perhaps show students something, then do something together with them, and then give them a practice exercise or two.
