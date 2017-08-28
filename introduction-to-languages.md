# Introduction to Languages

## Hardware advances

Over the last 20 years, computer hardware has seen exceptional growth in performance and stability.  In fact there is more computer horsepower on your cell phone than all the computers used to put a man on the moon.  As a result of this progress there is less of a focus on optimizing every little aspect of current software and the focus has shifted to increasing what software can do.

For much of the late 90's and early 2000's we saw a huge boom in processor technology then things tapered off until now. As we have approached some of the limits of what a single processor can do, there has been large gains in multi-core processor technology.  In short, since chips can't get much faster, the focus now is scaling them to work in clusters.  A simple example of this is using GPUs (Graphical Processing Units) to handle the workload of rendering graphics.  Even before this we saw the introduction of the 80486 (~1990) and it's included math co-processor.  At the time was a huge step as it set the ground work for multi processor systems by tasking a separate chip to deal with floating point calculations.  These advancements leads us nearly full circle, where now there _is_ a push to "work closer to the metal" in developing applications and patterns that can maximize the multi chip environment we now live in.

**References**

- [Markov Limitations, Nature](https://www.nsf.gov/news/news_summ.jsp?cntn_id=132339)
- [CPU Limitations, MIT Tech Review](https://www.technologyreview.com/s/421186/why-cpus-arent-getting-any-faster/)
- [History of CPU Power, WSJ](https://www.washingtonpost.com/news/the-switch/wp/2013/11/12/how-ridiculously-fast-our-computer-chips-have-gotten-in-one-chart/)
- [Moore's Law, Google](https://research.googleblog.com/2013/11/moores-law-part-1-brief-history-of.html)

## Overview of programming languages
**Machine**
A set of instructions that are executed at the chipset level. Usually specific to the hardware.  Most often originate as Assembly code and compiled for the desired chipset.  Machine code is encoded in a series of `0` and `1` set representing an explicit instruction or memory register.

**Assembly**

Assembly language is the human version of machine code.  Much of the instructions are the same, but it allows for mnemonic expressions of the instructions. For example on the [Zilog Z80](https://en.wikipedia.org/wiki/Zilog_Z80) chipset:

```
; Decrement register B by one
00000101         ; Machine
DEC B.           ; Assembly
```

**Middle (C)**

The C language has a long steeped history, and besides Assembly (and Machine) is one of the oldest languages that is still in use today.  Most of the current software and systems we have and use today are all built on top of C or its younger brother C++.  Originally developed in 1969 at Bell Labs, and since canonized by the ANSI and ISO committees since 1989, the C language is the backbone of all modern computers and most of the modern languages.  In most cases C code is portable among hardware architectures.

While the debate of wether C is a low level or "middle" language can be argued for some time to come, in most cases C is the closest one can get to the operating system without and the system hardware without the need of an intimate knowledge of the chipset located in the hardware.  Over the years, the C like syntax has become considered by many to be the gold standard of sorts, as it has evolved to be a readable language while allowing for efficient and effective static analyzers to perform tests upon the code.

C is also important because it can easily be pre-compiled to Assembly, and Assembly can easily be injected right into C code.

In recent years, there has been a significant push to move the development community away from C and strictly into languages that are "safe".  By some C is considered unsafe because it allows you direct access to memory, hardware and the system resources without much of a safety net.  What makes C so powerful is that is allows this, which means that a greater emphasis must be put on the developer to engineer safe code.

**High level**

While the entire computer world is built on the low level languages, the majority of the applications we used everyday are built in C (or some derivative there of), Java, JavaScript, Python, Fortran and a few others.  These high level languages are usually designed to fulfill a certain task and solve a certain kind of problem.  For example JavaScript is the language that every web application is built in.  Java offers a compiled language that runs in a virtual machine or container that can run on most computers, Python (originally a Perl replacement) has gained enormous support in the scientific and engineering world as tool for solving problems.  Fortran still remains the dominate math based language.  Nearly every mathematical centric software program has its roots in Fortran.

High level languages offer the developer a greater tool set to solve and resolve problems.  The syntax is often more forgiving and much of the grunt work involved in common tasks is handled by the languages compiler/interpreter.

Unless you are working in software engineering and/or specializing in performance optimizations of highly specialized programs, you'll more than likely always be working with high level languages.

**Source Code, Binaries, Compilers and Interpreter**

All computer programs begin as source code.  This is the code you write. All of the lower level languages and most often the lower the language the higher the likelihood that it uses a compiler to convert its source code to a binary.  Binary programs run much faster than an interpreted program.  Binary programs are also statically typed, which will be discussed later.  These two factors contribute to the performance and reliability that a compiled program offers.

There are many high level languages that are 'interpreted', meaning they are not compiled into a binary but compiled at run time or Just-In-Time (JIT) compiled.  Examples of these are any scripting language such as Python and JavaScript.  Some of the benefit of JIT languages is they allow for dynamic typecasting.  While there is valid arguments on both sides of the fence if dynamically typed languages belong in the professional languages quiver, it is important to always remember when using one to be diligent about what is being passed and assigned from variable to variable and functions, because much of the safety net of static typing is removed.

**Static vs. Typed**

Static languages require any variable or 'symbol' to be predefined as a certain type, whereas dynamic languages allow for symbol types to be changed during the execution of the program.

```
# Python example of dynamic casting of symbols

# Define and assign 'a' as an integer with the value of 1
>>> a = 1
>>> a
1

# Now re-define 'a' as a string with the value of 'Hello'
>>> a = 'Hello'
>>> a
'Hello'

# Pretty straight forward right?  Well lets cause trouble now
>>> min(1, 2, 3,)
1

>>> a = min(1, 2, 3,)
>>> a
1

# Right now 'a' is an integer value again, but we can change its symbol type
# to a function, since Python allows for functions to be first class citizens.
>>> a = min
>>> a
<built-in function min>

# Well that's kinda useful sometimes, but what about this?
>>> min = a
>>> min
<built-in function min>

# Ok, so no real harm so far because Python is smart enough to use pointers
to deal with this.  But lets look at this case:
>>> min = 'hello'
>>> min
'hello'

# Here we have re-casted the symbol 'min' to from a function to a string.
# Resulting in loss of access to the function via 'min()'.  The only way
# to re-gain the symbol would be to re-start the Python instance.
```

Static languages do not allow for any of this kind of Tom foolery.  Once the variable type is casted, it can not be changed.  Furthermore, static languages often offer an option to declare a variable as a constant, meaning that the value of the symbol can not change during runtime.

To my knowledge, the only dynamically typed language that offers a 'constant' argument right now is JavaScript ES6, but future versions of Python and others may eventually include this safety mechanism.


**Choosing a language for a task**

> To a hammer, everything is a nail

It is important to use the right tool for the job and not force a tool that is not meant for a task to complete that task.  For example, you would not use C to write a simple program to read data from a text file and graphically plot that information, whereas it would not be prudent to use Python to write mission critical software for a satellite.

Programming at is core is just solving problems using logic and once you learn how to solve a problem logically, writing the code is a matter of learning some syntax rules. "Logic is Logic, syntax is whatever", Chris Galli.

Spend some time learning about the current languages out there, and the ones relevant to your discipline.  Sometimes when working on a complex project, you may find the need to use say Fortran to model something and Python or NCL to plot images from it.
