# Introduction to Control Structures

> A computer can only do one of two things: turn on or turn off.

## Types of control flow

There are three basic types of program control flow.

- Sequential, executes statements "procedurally"
- Selection, involves making a decision
- Repetition, repeated task

### Sequential

Sequential flow simply executes one statement after another.  Often called "procedural" or "do this, then that" programming.  

It is important to keep in mind now that the term "procedural" has taken somewhat of a different meaning now that many computer systems use asynchronous programing patterns.

```python
# Example of sequential code:
a = 42
b = a + 36;
return b;
```

### Selection

A selection statement defines when the program needs to make a decision.  Since a computer understands nothing but boolean logic, every decision that it makes must be composed of simple "Yes/No" (true/false) decisions.  In nearly every language the following selection scenarios are available to use to instruct your program what to do at a crossroads.

- `if`
- `if/else`
- `if/else if/else`
- `switch` (varies in application per language)

#### `IF` statement

![flowchart IF][if-then-1]

```python
# Simple IF statement
b = 5
if a > 78:
    b = 10
```

#### `IF/ELSE IF/ELSE` statement

![flowchart IF][if-then-2]

```python
# Simple IF/ELSE IF/ELSE statement
b = 5
if a > 78:
    b = 10
elif a < 100:
    b = 0
else:
    b = 1
```

#### `switch` statement

Derived from the `IF/ELSE IF/ELSE` construct.  Varies in application per language, but evalutes the same value against several statements and 'stops' on the first match.


### Repetition

Repetition controls are used to repeat a portion of the code until an instruction to stop is passed.  Commonly seen methods of this are:

- `while` (`do/while`)
- `for`

At the most logical level, these are essentially the same command, and in most places can be interchanged for each other.  The key difference is how the loop is terminated.  A `for` loop is terminated after a pre-defined number of iterations, whereas a `while` loop will execute until an explicit command is passed to exit the loop.  While modern languages often offer "escape" arguments to a `for` loop, it is best to avoid using these unless absolutely necessary.

```python
# Python for loop
for i in xrange(10):
   print i
```

```python
# Python while loop
while (i < 10):
  print i
```

![][loops]


## Designing/planning out a program

> There are two hard things in computer science: cache invalidation, naming things, and off-by-one errors.</p>&mdash; [Jeff Atwood (@codinghorror)](https://twitter.com/codinghorror/status/506010907021828096)

In my experience, programming is simple, solving the problem is the hard part.  Meaning that once you learn the basic mechanics of programming, applying that to a language is fairly straight forward.  The real challenge of programming is:

- understanding the problem
- breaking the problem down to small parts
  - breaking those small parts into smaller parts
    - breaking those smaller parts into even smaller parts
      - avoiding [recursion][recursion]
- writing code that not only you can understand but so can the next person

At the onset of any program it's pretty important to have a clearly defined set of goals.  It is far too easy to start working on a project and before you know it, the code you're working on is doing something completely different than what you expected.  Remember it's better to write smaller simpler programs than larger complex ones.

Two of the most common ways people often get a program started is to "whiteboard" the problem.  White-boarding is when you draw out the program and what it needs to do and roughly how it will do it.  Many times a combination of "pseudocode" and "flow-charting" are used in this process.

![whiteboard-example][whiteboard-example]


## Logic

As we've already discussed, computer can only turn on and off.  Therefore all the logic within one has to be of the boolean nature.  Now, at the language level, these can be expanded to include **logical operators**.  In the end these all result in a boolean response.

In all languages the logical operators behave in accordance with the rules of traditional mathematics.
```c
// These examples are using the 'C' style notation which
// is common in many languages.

a == b        // a is equal to b
a != b        // a is not equal to b
a < b         // a is less than b
a <= b        // a is less than or equal to b
a > b         // a is greater than b
a >= b        // a is greater than or equal to b

// Furthermore, there are boolean operators...
a && b        // 'AND', true if both a and b are true
a || b        // 'OR', true if either a or b (or both) are true
!a            // 'NOT' (negation), true if a is false
```

In all languages a logical expression is evaluated from left-to-right.  This allows for a process called 'short-circuit' to be introduced whether intentional or not.  This class will not focus on this.


## Parting shot

It's better to take a few extra minutes when starting out to solve the logic puzzle of your program than trying to do it as you go.

<!-- Refs -->
[if-then-1]: supplementary/if-then-1.png
[if-then-2]: supplementary/if-then-2.png
[loops]: supplementary/loops.png
[whiteboard-example]: supplementary/whiteboard-example.png
[recursion]: https://en.wikipedia.org/wiki/Recursion_(computer_science)
