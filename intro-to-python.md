# Introduction to Python

> Python is a flexible language for a `list` of uses.

## History of Python

> Over six years ago, in December 1989, I was looking for a "hobby" programming project that would keep me occupied during the week around Christmas. My office ... would be closed, but I had a home computer, and not much else on my hands. I decided to write an interpreter for the new scripting language I had been thinking about lately: a descendant of ABC that would appeal to Unix/C hackers. I chose Python as a working title for the project, being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus). ~  [Guido van Rossum](python-foreword), 1996

This quick history of Python is similar to many other niche languages, where the creator was tired of another language and decided to make a new one.  What happened with this one though is it took off as it opened the door to many non-technical programmers to leverage computing power for their needs.

so BOOM, we got...

![Python logo][python-logo]

At the core of python is a "single, obvious way to code...", meaning that when Van Rossum designed the language he wanted a language what was readable similar to literature.  Keeping this in mind as we move foreword with Python, its important to learn the patterns set forth by the Python governing body (Python Software Foundation), as they have decided that there is basically one way to do things, unlike other languages like C/C++, Fortran, JavaScript and many others where there are countless ways to solve a problem.

To further support my editorial:

```python
import this
```

Over the years Python has become a go-to language of the science and engineering community where the application is non-mission critical.

Regardless how we got here, we are here now, so lets learn some Python!

## First steps

Unlike MATLAB or IDL, Python is programming language without an IDE (Integrated Desktop Environment).  This is both a blessing and a curse depending on the situation in which you need to work.  Python is a scripting language, so there is no need to compile it, but you still need to tell the Python "compiler" to interpret the program.  This is simply done by using the command line and something like this:

```bash
$ python hello.py
```

This will execute the `hello.py` script on the current thread.  While it is possible to connect Python to a "debugger", that is outside the scope of this lesson.  We will learn some debugging techniques that use the command prompt.

In order to get going, you will need to use a text editor, this can be _any_ text editor that supports ASCII text.  Some common ones used right now are [VSCode](vscode), [Atom](atom), [Sublime Text](sublimetext) and [Notepad++](notepad++).  These modern text editors are really nice to work with since the allow for syntax highlighting, linting, error checking, intellisense, etc.  It does not matter which one you use, just use one that you feel comfortable with.  You can also use `vi` or `nano` if you are working in the CHPC space.

There are also programs such as [Spyder](spyder) and [PyCharm](pycharm) that attempt to be Python IDEs but they are often difficult to work with.

> For the live demos, I will be using VSCode and a terminal window.

## `Hello World!`

As with all programming languages, the most classic program is **hello world**, so here we go.

```python
meaning_of_life = 22 * 2
print 'Bonjour le Monde!'
print 'The meaning of life is %s' % meaning_of_life
```

and the expected result:

```bash
$ python hello.py
Bonjour le Monde!
The meaning of life is 42
```

### Basics of the Python syntax

At the very code of Python's language design is the ability to be easily readable.  This is the rational behind the lack of line terminators, control blocking and a sternly recommended line length.  Furthermore Python is also a dynamically typed language meaning that a variable can change `type` as the program progresses.

**Indicate a comment**
```python
'''Block comment, also knows as a "Docstring"'''

'''
    Block comment
    with multiple lines
'''

# Single line comment
a = 78  # Inline comment
```

**`print` something**
```python
print 'My name is Adam'

name = 'Adam'
print 'My name is %s' % name  # Using template literals

# Using multiple variables and escape characters
dogs_name = 'Dixie'
print '%s\'s dog\'s name is %s' % (name, dogs_name)
```

**Declare a variable**

> Python is dynamically typed. Please read **Static vs. Typed** [here][intro-to-languages].

```python
variable_name = value
```

**Arithmetic operation**
```python
# Eligible operators: + - / * %
print 22 * 2

# using variables is pretty easy
two = 2
meaning_of_life = 3274 / (two * 22)  # Should equal 78
```

**lists and dictionaries**

Think of **lists** as linear arrays and **dictionaries** as collection of items.  Both of these are very powerful tools to organize and deal with data and mutable storage.

```python
# --- Working with lists ---
# Unlike arrays in other languages, lists can be mixed typed.
a_list = [1, 2, 3]  # A list
print a_list[1]     # should be 2
a_list.append(4)    # 'appends' 4 to the end of the list
print a_list        # should be '[1, 2, 3, 4]'

# --- Working with dictionaries ---
a_dict = {
    'name': 'Adam',
    'dogs_name': 'Dixie',
    'rescue_dog': True
}

print a_dict['dogs_name']     # should be 'Dixie'
a_dict['rescue_dog'] = False  # which is false

# !!! Be warned of Python's object linking (pointers)
#     In order to break the connecting pointer you need to
#     deep copy the value
#     https://docs.python.org/2/library/copy.html
a = {'x': 1}
b = a
print b  # should be {'x': 1}
a['x'] = 9
print b  # should be {'x': 9}
```

**Sets**

A **set** is a non-mutable **list**.  Once a set is "set" it can not be altered.

**`if`, `elif` & `else`**
Any Python control block uses a four (4) space indent to indicate the control block.  **Do not use tabs!**

```python
if 1 == 1:
  print 'I hope so'

thing_1 = True
thing_2 = False

# Single if/then
if thing_1 == thing_2:
    print 'I hope not'

# A complete if/else if/else
if thing_1 == thing_2:
    print 'Thing 1 is equal to Thing 2'
elif thing_1:
    print 'Thing 1 is True'
else:
    print 'Thing 1 is NOT equal to Thing 2, and Thing 1 is NOT true'

# What should this be?
print 'Yep' if thing_2 else 'Nope'  
```

**`for` loop**

```python
# Iterates over each element in 'numbers'
numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
for item in numbers:
    print item

# Iterates over the position in 'numbers'
# Why is this sometimes the better option than the previous method?
for idx in xrange(len(numbers)):
    print numbers[idx]

# Plain on 'for loop'
for i in xrange(10):
    print i, i * 2
```

**`while` loop**
```python
# Trivial example
while ping_pong:
    ping_pong = False if ping_pong else True

# Have an escape plan
count = 0
while ping_pong:
    if count == 0:
        ping_pong = False

# Bad idea
while 1 == 1:
    print 'We will never get out of this loop'
```

### Put all this together ...

Let's write a simple program to calculate the Fibonacci Sequence.  There are several ways to do this, some use lists and some don't.  The following example uses a list to track the variables needed to calculate the next value.

> HOMEWORK: You will need to re-write this not using lists or dictionaries.

```python
'''
Fibonacci Sequence using Lists

The Fibonacci Sequence is the sum of the last two numbers.
    0, 1, 1, 2, 3, 5, (and so on) ....
'''
fib_sequence = []  # where we store the results
for i in xrange(10):
    if i < 2:
        fib_sequence.append(i)
        continue

    fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

# Print the results
# Also introducing the 'map()' function which applies
# a function against list.
print 'The Fibonacci Sequence is:\n%s ...' % ','.join(map(str, fib_sequence))
```

## In closing

These are the fundamental building blocks of Python.  There are more advanced and clever ways to do some of these things, but nearly all problems you'll encounter will use these basic tools.  The more you program, the better you will become at knowing which tool to use.

<!-- Refs -->
[python-foreword]: https://www.python.org/doc/essays/foreword/
[python-logo]: https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png
[vscode]: https://code.visualstudio.com/
[atom]: https://atom.io
[sublimetext]: https://www.sublimetext.com/
[notepad++]: https://notepad-plus-plus.org/
[spyder]: https://github.com/spyder-ide/spyder
[pycharm]: https://www.jetbrains.com/pycharm/
[intro-to-languages]: ./introduction-to-languages.md
