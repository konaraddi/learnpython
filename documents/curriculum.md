# Timeline

#### `001_helloworld.py`

#### `002_object_types.py`

#### `003_expressions.py` <- I'm here

### 3. Expressions, Objects, and Variables

You can assign expressions and variables (both are objects) a name.

Computers can't solve equations like `3 + x = 2` but then can solve expressions like `3 - 2`.

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
