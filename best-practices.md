# Some Best Practices

## Basics

> "Good programming style begins with the effective organization of code. By using a clear and consistent organization of the components of your programs, you make them more efficient, readable, and maintainable." -- Steve Oualline, C Elements of Style

At the most basic level of any good program is an intuitive layout of the functions along side effective documentation. Syntax varies across all languages but the overall process in which a computer executes the code is the _same_ across all languages. In this section we will discuss the foundations for robust programming techniques, how to document code to assist in its longevity. Most of the guidelines presented here are sourced from code standards from NASA, ECMA and ISO agencies. While your code may not be destined for NASA or another mission critical operation, you should adhere to them as they will teach you industry standard and proven methods and practices, you never know when you might need to include some code you wrote earlier in life in a project later on. Standards allows you use reuse code in a consistent manor. You will often find many different and clever solutions to a problem, but be wary of methods that can destabilize a system.

## Comments and Code Clarity

![Apollo Comments](http://pop.h-cdn.co/assets/16/28/1468253829-screen-shot-2016-07-11-at-121632-pm.png) [Source](https://github.com/chrislgarry/Apollo-11/blob/master/Luminary099/BURN_BABY_BURN--MASTER_IGNITION_ROUTINE.agc#L39-L45)

You might have the most elegant and optimized code ever written on the face of the earth, but without comments, your code is worthless. Good documentation within (and around) your code is how you communicate what the program does and how to use it. At a deeper level it tells you future user (or yourself in the future) how the code is intended to be used. Good code comments are more of a dialog rather than a series of short one liners that explain the obvious.

Take your classic `hello world` example. In the first example We have line by line explanation of the code, where in the second example we have a simple explanation of what the program does.

```c
/** All inline comments */
int foo() {
    // Print `Hello World` to the user.
    cout << "Hello World!" << endl;

    // Send exit signal back.
    return 0;
}
```

```c
/** Dialog style comments */
int foo() {
    // Prints `Hello World` to the user, then sends exit signal.
    cout << "Hello World!" << endl;
    return 0;
}
```

We can further clean this up by using _Java_ or _Doxygen_ style comments. This style of commenting allows a code preprocessor to glean a substantial amount of information from your source code that can be converted to documentation as well as accessed by the toolchain in most editors to give the programmer insight into how the code works. Lets re-write our little hello world function using standard Doxygen comments.

```c
/** JavaDoc style headers */

/**
 * @brief   Prints `Hello World` to the screen
 * @author  This guy
 * @returns {integer} - exit code. Default of `0`.
 */
int foo() {
    cout << "Hello World!"" << endl;
    return 0;
}
```

Please read _ASTG Coding Standard_ chapter 7 for more information on NASA's preferred method of documenting code. This standard has been adopted widely in the computer industry with only a small change of often dropping the `@brief` tag as most document generators accept the first line of text as the object brief. The Python documentation standard is similar in concept just a slightly different method of documentation. Please read the [PEP8 standards](https://www.python.org/dev/peps/pep-0008/).

Before a riot starts, not all comments need to be moved to the routine's header. Inline comments serve a very valuable purpose. These help to explain what is happening at that location (or moment) in the code's execution. For example:

```
;!
; @brief   Calculate co-longitude boundary coordinates that cross the meridian
; @author  Adam C. Abernathy
; @version 1.0.0
;
; @param geo_lon {array<float>} - Longitude(s) to compute
; @param elon {float} - eastern boundary limit
; @param wlon {float} - western boundary limit
;
; @return {array} - Co-longitudes of `0-360` degrees
;
function calculate_co_lon, geo_lon, elon, wlon
    compile_opt idl2

    ; Western longitude
    co_wlon = wlon
    if co_wlon lt 0 then co_wlon = co_wlon + 360.0

    ; Eastern longitudes
    co_elon = elon
    if co_elon lt 0 then co_elon = co_elon + 360.0

    ;  Now convert the entire geo_lon arrays
    co_geo_lon = geo_lon

    ;
    ;  Using a matrix operation rather than a for-loop, find the values
    ;  on the western side of the Prime Meridian
    ;
    result = where(geo_lon lt 0, count)
    if count gt 0 then co_geo_lon[result] = co_geo_lon[result] + 360.0
    all_co_geo_lon = co_geo_lon

    return, create_struct('co_lon', co_geo_lon,
                          'co_llon', co_wlon, $
                          'co_rlon',  co_elon, $
                          'err_code', 0)
end
```

We can see that the function header indicates how to use function and the expected response, the inline comments communicate with another programmer what the intent and expected actions are.

## Spaces vs. Tabs

The tabs versus spaces argument is about as old as the computer its self. Well since we moved from punch cards to the freeform code file. Many have argued that tabs are superior to spaces since they allow you to determine your indentation level and they consume less storage space.

In reality we find that theory and practice are never the same in this case. When multiple people (or editors) use a file you will often find a mix of tabs and spaces within the file which creates a plethora of confusion and often unreadable source code. A majority of modern code standards have moved to spaces only. The default is 4 spaces per "tab" except in Fortran which is 3 spaces.

Use spaces. Period. Set them to 4\. End of story.

Furthermore there is much ado about bracket styling. Most agree that Kernighan and Ritchie bracing style is the standard. While there is some flexibility here in this method, the important thing is to continue what the original author of the project started with. **Regardless if the language lets you omit the brackets,** always **include the brackets**. The same applies to line terminators.

The following examples of bracket usage are pretty common.

```javascript
function foo(args) {

    // If `args.bar` is undefined then set to `bar`, else print passed value.
    if (typeof args.bar === "undefined") {
        args.bar = "bar";
    }
    else {
        console.log(args.bar);
    }

    // Determine if the optional argument is passed and if correct then
    // give the user a message.
    if (typeof args.generalSolution !== undefined && args.generalSolution == 42) {
        console.log("You are wise.");
    }

    return true;
}
```

It is also commonly acceptable to use the following:

```javascript
function foo(args) {

    // If `args.bar` is undefined then set to `bar`, else print passed value.
    if (typeof args.bar === "undefined") {
        args.bar = "bar";
    } else {
        console.log(args.bar);
    }

    // Determine if the optional argument is passed and if correct then
    // give the user a message.
    if (typeof args.generalSolution !== undefined && args.generalSolution == 42) {
        console.log("You are wise.");
    }

    return true;
}
```

## Ternary logic & operators

You may come across code that looks like this

```javascript
var A = B === true ? "yep" : "nope";
```

Or the Python version...

```python
is_here = True
wheres_waldo = "here" if is_here else "lost"
```

And the Fortran (90+) version of it...

```fortran
this_value = merge(x, y, a > b)
```

You will often find this type of programming in optimized code especially when someone has gone to the pains of creating a truth table to guide the decision flow of the program. The key take away here is these operators are often faster to execute, sometimes harder to read and exists when something can only have two states at a time. The general format is always:

```
variable = expression <true> <false>
```

## Cases and naming conventions

This is another are of hot debate. The general solution here is to use what your industry prefers or ideally what the language maintainers recommend the language look like. The **camelCase**, **PascalCase** and **snake_case** formats all mean different things in different languages. Below is a table of the common applications for them in some of the languages you might encounter .

Identifier                                   | Python     | C/C++      | Fortran & IDL           | JavaScript
-------------------------------------------- | ---------- | ---------- | ----------------------- | ----------
Variable, Keywords                           | snake_case | camelCase  | snake_case              | camelCase
Namespaces, Classes, Interfaces & Exceptions | PascalCase | PascalCase | PascalCase              | PascalCase
Methods, Functions & Subroutines             | snake_case | camelCase  | snake_case or camelCase | camelCase
Constants                                    | ALLCAPS    | ALLCAPS    | ALLCAPS                 | ALLCAPS

## Power of 10

Laid out by JPL lead scientist Gerard J. Holzmann, these strict coding rules focus on security.

NASA's 10 rules for writing mission-critical code in a simplified form:

1. Restrict all code to very simple control flow constructs – do not use `goto` statements, `setjmp` or `longjmp` constructs, and direct or indirect recursion.

  - _Ideally you want all your code to be easily maintainable and verifiable. By reducing complex loops, removal of all `goto` style statements and implementing as much ternary logic as possible your source code becomes far easier to maintain and diagnosable when problems do arise._

  - _As for the recursion topic, this is a hotly debated issue. In short most languages support recursion, but due to the way the stack is handled and the possibility of the "endless rabbit hole", it is best to steer clear of using recursion._

  - _This is a pretty important rule to follow when writing code that will be moved into a production environment, as it is standard now to use a [Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration) engine or [Linter](<https://en.wikipedia.org/wiki/Lint>_(software)) at every stage of the software build process._

2. All loops must have a fixed upper-bound. It must be trivially possible for a checking tool to prove statically that a preset upper-bound on the number of iterations of a loop cannot be exceeded. If the loop-bound cannot be proven statically, the rule is considered violated.

  - _Pretty self explanatory. If you are using a C style loop then you do not need to worry. This is a safeguard against run-away `while` loops and recursive statements._

  - > "By having upper limit bound, the function can recover from an error state and return then program to operational state."

3. Do not use dynamic memory allocation after initialization.

  - > This rule is common for safety critical software and appears in most coding guidelines. The reason is simple: memory allocators, such as malloc, and garbage collectors often have unpredictable behavior that can significantly impact performance. A notable class of coding errors also stems from mishandling of memory allocation and free routines: forgetting to free memory or continuing to use memory after it was freed, attempting to allocate more memory than physically available, overstepping boundaries on allocated memory, etc. Forcing all applications to live within a fixed, pre-allocated, area of memory can eliminate many of these problems and make it easier to verify memory use. Note that the only way to dynamically claim memory in the absence of memory allocation from the heap is to use stack memory. In the absence of recursion (Rule 1), an upper-bound on the use of stack memory can derived statically, thus making it possible to prove that an application will always live within its pre-allocated memory means.

  - _In short, be diligent when managing your variables. While most of the interpretive languages do most of this work for you via garbage collectors, you should always be proactive in managing memory. **It has been noted in the current ASTG standards that the recommended practice for declaring variables is near the location in which they will be used**._

  - _It is also important to not recast variable types once initialized. This is easily doable in interpretive languages but is not recommended, because of how the memory is allocated for different types of variables._

4. No function should be longer than what can be printed on a single sheet of paper in a standard reference format with one line per statement and one line per declaration. Typically, this means no more than about 60 lines of code per function.

  - > Each function should be a logical unit in the code that is understandable and verifiable as a unit. It is much harder to understand a logical unit that spans multiple screens on a computer display or multiple pages when printed. Excessively long functions are often a sign of poorly structured code.

  - _In reality you may have functions that are longer, especially when good documentation accompanies the code, but the idea is that each little piece of you code should be easy to read, and maintain._

  - _I would also add that most code styles have a line length standard to. For example Python's PEP8 standard requires a 79 character line limit. Most other guides have either a 80 (classic) or 100 character per line limit. This provides easy readability on most computer screens._

5. The assertion density of the code should average to a minimum of two assertions per function.

  - > Statistics for industrial coding efforts indicate that unit tests often find at least one defect per 10 to 100 lines of code written. The odds of intercepting defects increase with assertion density.

  - _Basically write unit tests. This can be a pain to do, but will save you from plenty of headaches down the road. Ideally for this rule you should have two unit tests per function. You should also expand your number of tests for known fringe cases. Run these tests at every major build and you'll be able to track up and downstream consequences of a change in your code._

6. Data objects must be declared at the smallest possible level of scope.

  - _The idea here is to keep data scoped at the lowest possible level. Doing this assists your static checker (lint), reduces memory overhead and by privatizing variables you reduce problems such as clobbering and collisions._

7. The return value of non-void functions must be checked by each calling function, and the validity of parameters must be checked inside each function.

  - > This is possibly the most frequently violated rule, and therefore somewhat more suspect as a general rule. In its strictest form, this rule means that even the return value of printf statements and file close statements must be checked.

  - _This is one of the most critical of the rules, because you can eliminate several issues just by running simple error checking at the start of the function as well as verifying the return at the caller. Essentially every caller can become a mini unit test of sorts._

  - **In my experiences this is one of the simplest rules to follow, and has saved me hundreds of hours of debugging and expedited every code review I've been a part of.**

8. The use of the preprocessor must be limited to the inclusion of header files and simple macro definitions. Token pasting (**code pasting**), variable argument lists (ellipses), and recursive macro calls are not allowed. All macros must expand into complete syntactic units. The use of conditional compilation directives is often also dubious, but cannot always be avoided. This means that there should rarely be justification for more than one or two conditional compilation directives even in large software development efforts, beyond the standard boilerplate that avoids multiple inclusion of the same header file. Each such use should be flagged by a tool-based checker and justified in the code.

  - _While preprocessors are often used (and valuable) in the build process for many languages and they can easily obfuscate code and "destroy code clarity and befuddle many text based checkers"._

9. The use of pointers should be restricted. Specifically, no more than one level of dereferencing is allowed. Function pointers are not permitted.

  - _Pointer are powerful and yet can cause all sort of problems if not used correctly. In this context they are referring to C/C++ and Fortran, but it is important to note that Java, Python, IDL and even JavaScript use pointers behind the scenes. In many interpretive languages when you copy a object in effort to save memory and improve performance the compiler creates a pointer to the original object._

10. All code must be compiled, from the first day of development, with all compiler warnings enabled at the compiler's most pedantic setting. All code must compile with these setting without any warnings.

  - _When writing software, don't hide warnings, delay fixes etc. Always resolve runtime errors, exceptions and any other issue as you write the code_

Some parting words from NASA:

>> The rules act like the seat-belt in your car: initially they are perhaps a little uncomfortable, but after a while their use becomes second-nature and not using them becomes unimaginable.

## Version control

As much as I would like to teach a segment on Git and its amazing powers to save not only your sanity but allow you to communicate with other programmers anywhere in the world, this class does not have the time to do that. You can find notes from my short course available **here**. Regardless whether you use SVN or Git (do not use SVN), you should get on deck with some form of version control at the start of your project. Git is just how things are done these days.

Git is based on a full distributed branch model of source control. At the heart of Git is the `diff` command from Unix. This is only fitting since Git was invented by Linus Torvalds himself. If you've ever used `diff` on your computer then you will be right at home using Git.

Like all things, using Git requires a workflow that you adhere to, while you can evolve your overall "build to deploy process", the basics of using it are basically the same. Since `diff` is the heart of this, the _commit_ is central to version control. A _commit_ is nothing more than a snapshot of what has changed since your last commit.

The basic workflow goes as follows:

1. Make some code changes
2. Make a git commit
3. Make some more code changes

A key part of the Git workflow is the process of "commits". A commit takes a snapshot of the changes to the repository and stores them in a database (located in the `.git` folder). These snapshots can be reconstructed to restore the project to an earlier state as well as lets you easily see the changes from stage to stage of the project.

Ideally you want to create commits often as this helps to create a solid timeline of the progress of the project. **If you give descriptive commit messages, then you can quickly locate problems in your code where things ceased to work as expected.**

To make a commit to your repository just do the following from the command line

```
git add .
git commit -m "Changed the equation for dew point"
git push -u origin master
```

Lets break down what is happening here. First we `git add .` this just tells Git to track all the files in the folder. Next we commit the code to the repository with the `git commit -m "Blah"` statement. **You must have a message for every commit.** You'll want to give this a descriptive title so you'll be able to make sense of the message later on. Also, this title must be less than 72 characters long. I'll explain why later. Lastly the `git push -u origin master`, pushes the code to your Git server. The `-u` means "upstream", `origin` is the URL (we defined this earlier in the `remote add` statement) and `master` is the branch to push the code to.

Gitting (great pun huh?) a repository from another user is really easy. If the code has been hosted on a service like GitHub, GitLab or something similar, you can just `clone` into the repo with `git clone <url here>` and you're ready to start working.

If you want to start your own repository, simply navigate to the root folder of your project and type `git init` and you're ready to go.

One of the most powerful tools in git is the ability to use branches, create logs and revert to a previous commit. All of these allow you to have full control over your source code and easily revert to a previous change when your code still worked.

## Pseudocode / Program flow and design

[Pseudocode](https://en.wikipedia.org/wiki/Pseudocode) is the process of putting your ideas about your program on paper (or screen). This can be done in several ways, some of these include flow charts, [Warnier diagrams](https://en.wikipedia.org/wiki/Warnier/Orr_diagram), [UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language) or just plain english statements that say what you are going to do.

![code1](img/code1.png) _From "Logic and Structured Design for Computer Programming", 3rd Ed., Harold J. Rood_

In my experiences the most common formats are flowcharts and descriptive paragraphs that explain the problem and a few basic steps to solve them. It is also pretty common to just write out a few comments in your code to start the overall process. Personally I use a notebook and sketch a flow chart then transfer those notes to comments in the code. I expand the comments to paragraphs of text that explain what the code should be doing.

This is the perfect to time to try and distill your logic sets down to a the most concise possible as well as you will start to get a feel of how you should break apart the program in terms of functions and scoping. This process also helps you identify points of failure and ways to mitigate them.

## Your program's API

The way in which you or other code an programmatically interact is called the API. API is short for Application Programming Interface. You will want to carefully think about what options are surfaced here and the overall schema that you use so your code can be easily reused.

"Surfacing" an option means that the user without modifying the source code can alter that portion of the program at runtime. I find it's best to be minimal at first then add extra options as you find the need for them. Once you push code that has a given API it's difficult to resend the feature, since downstream you might have been using that feature.

## Flowcharts

Flowcharts are probably the most common tool for diagraming and sharing the diagrams with others. We've all seen something like this before.

![Good Code: xkcd](http://imgs.xkcd.com/comics/good_code.png)

For the most part these symbols are intuitive but long time ago, [IBM made an effort to standardize](http://www.eah-jena.de/~kleine/history/software/IBM-FlowchartingTechniques-GC20-8152-1.pdf) them

![IBM flowchart symbols](img/ibm_flow_symbols.png)

<!--
_Class problem_

### Pascals Triangle

A classic problem to solve is [Pascals triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle).

![Pascal's triangle](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

Let's solve it using the binomial theorem. -->

### Scoping

![GOTO: xkcd](http://imgs.xkcd.com/comics/goto.png)

- Since the advent of function based programming languages, we have the ability to create reusable code. Ideally you want to localize your variables at the lowest level. This removes them from the global namespace.

- Sometimes you do want variables in the global space, these should be things like constants and globalized parameters.

### Classes

Most languages have a Class or Module pattern that allows for grouping of functions to accomplish a task. Fundamentally, a class has a `constructor` that initiates the class at a given state. Classes often possess `public` and `private` members also. This allows for encapsulation of variables and reduces namespace pollution.


## Parting shots

> You show me a program that doesn't have any bugs and I'll show you program that doesn't do a thing.

It is considered impossible to write semantic code using all the best practices and idioms while having a program that does anything.  But not all is lost, by using what we've talked about here, you can write code that is portable, maintainable, diagnosable and easy for others to understand.  You should write your programs with the same rigor that you would write a journal article with.  In essence when you paper is being peer-reviewed, so is your program.

> The ultimate take away here is you need to always know what your program is doing.
