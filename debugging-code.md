# Debugging

> Unless you're me, your code is going to have bugs in it. Why is my code flawless you might ask? It's because I follow TDD, semantic versioning, proper source control and all the best practices. ~ Every programmer ever

Debugging in its simplest context is the art of detecting and solving bugs within the code. While there are some very scientific approaches to this, it is truly an art form one has to hone over years of practice and intuition.

>> Mr. Edison, I was informed, had been up the two previous nights discovering 'a bug' in his phonograph - an expression for solving a difficulty, and implying that some imaginary insect has secreted itself inside and is causing all the trouble. ~ [The Oxford Dictionary](https://en.oxforddictionaries.com/explore/was-the-first-computer-bug-a-real-insect)

The simplest idea is to put a series of log statements track the progress of your program and the state of a variable of interest. While this is the most common way to solve diagnose problems, this method is not the best for when are running your code in a production environment (or in the wild). Ideally when you write code, it is recommended that you add "tracers" or in other words, some form of output indicators that can give a diagnostic picture of the program's state. Most often these messages are sent to an error buffer or a runtime log file and then destroyed at the end of the execution.

Every language has a different preferred method of debugging and logging errors, but the general idea is the same. When running in a diagnostic mode: be continually sending messages to a log file.

## Semantic Methods

**Variable types**

> Is this an apple or an orange?

A common error is simply thinking you have a float but really you have a double. Or you think you have a number and you have a string. Again unit testing and response verification can alleviate many of these problems.

Since static languages don't allow you to change the variable type, you'll need to make sure you choose an appropriate variable type. Since dynamic languages let you change the variable type as you go, be wary of changing the variable type as you move through the code.

It is also prudent to _type guard_ inside your receiving functions. Type guarding is simply testing the variable type before you use it. This is also the ideal time to recast the variable if needed. Ideally, if you recast the variable assign it to a new variable.

```python
def foo(_a):
    # Test to see if the arg passed is a string
    if _a is None:
        print "No argument passed, using default"
        a = "Hello Denizen"
    elif type(_a) is not str:
        a = str(a)
    else:
        a = _a
    # ...
```

From the above example, you can see that we test to see if the variable even exists. If we don't have a variable, then clearly we need to either use a default value or you could bail out. If you bail out, you should send back a _null_ or _NaN_ back to the caller, this way you can verify the response. Your unit test cases should pass and expect these fringe cases too.

There is an entire category of functions called "sanitizers". Sanitizers provide a systematic way to scrub all your incoming data and ensures that it meets the variable type and desired precision. These functions are nothing more than glorified type guarding routines.

**Sanity Test**

> Is what I'm doing make any sense?

![random number](http://imgs.xkcd.com/comics/random_number.png)

You can only rely on static checking to diagnose logical, systematic or syntax errors.  The sanity test is knowing and being realistic about what your code is actually doing and where it is heading.  Sometimes just stepping back and looking at the larger picture of what is happening can often reveal that the approach, method and or science involve in your code is flawed.

_Personally I after ensure my unit tests passed, this is my next step._

**Unit Tests (TDD)**

> Before you code, write the unit test

Test Driven Development or just TDD, is the practice of always writing the unit test _before_ you begin to write the code to perform whatever it is you want to perform. In most circles now, this is the defacto standard in programming. For example, if you had a function that adds 5 to every number input or returns a null value if it's not a number, then you would write the unit test for that first before you wrote the function "add5". By using this practice, you are forced to keep in mind _"What should the problem solve?"_ which helps to prevent the down the rabbit hole experience of trying to solve a problem you lost sight of. Furthermore by setting expectations for the output of your code ahead of writing the code, you automatically force your new code to match the API of your existing codebase, because you know the expected outcome and its validity.

Automated testing (unit tests + TDD) allows you to test multiple cases and scenarios quickly and systematically. Also, once you have defined these cases, you can test them by simply calling your test routine. I have found this extremely valuable when testing fringe cases or complex to diagnose problems. If you can isolate the input to your function (which you should since they should be **pure** functions anyway), you can easily test and flag/mask fringe cases.

> Unit testing and verification can prove the presence of faults, but lacks the ability to prove there are no faults.  This being said, the more you test, the list of problems is reduced giving you confidence that the executed code is sound and performing as expected.

Refactoring becomes a manageable task. We write code, then add, modify, append all the time. Over time, our codebase needs to be cleaned up, or we find a better way to do things. Often the case without TDD tactics, you either have to do a complete re-verification of the codebase or you simply just assume it works. Both of these are impractical and/or unsafe. When using a TDD approach, you can edit any code that is testable, then simply run your testing routines to verify its result, and your done. You know for sure that the code is sound.

Fear of breaking code upstream or downstream is reduced if not removed. By having fully testable code, you don't have to worry about changing something in one place and breaking code in others. You'll immediately know if the new code affects something elsewhere. Although if you write pure functions you can eliminate this problem.

```python
def add5(n):
    r"""Adds 5"""

    if type(n) is int or type(n) is float:
        return n + 5
    else:
        return None


def test_add5():
    r"""Unit test for `add5`"""

    print "Testing add5()..."
    print add5(0) == 5
    print add5(-1) == 4
    print add5(1) == 6
    print add5(1.1) == 6.1
    print add5("4") == None
    print add5({}) == None
```

_What is another test that should be checked for?_

**Response Verification**

> I paid for an apple, but I got an orange

Ideally at this point you've accepted the argument that a unit testing based approach to code writing is the safest and most efficient way to write and test code. But using TDD is not just writing some witty scripts to validate some functions and only run every now and then. The key concept here with TDD is you test and validate all values and arguments before and after they are passed.

> > If you functions upon error return a null state, then you can intelligently make a decision as to what to do about with your response.

## Runtime Methods

**"Step And Print"**

> What are you doing right now?

This is by far one of the most commonly used methods. You place print statement in your code and see what the result is.

**Diagnostic & auxiliary files (Log files)**

> A little paperwork goes a long way

Expanding on the "Step and Print" tactic, log file entries are added at critical points of the program. Often an entry is made whenever a `try/catch` statement is caught. It is a very common practice to add a "debug" or "verbose" mode to your code, that logs or displays nearly every major variable and logic gate as it modified throughout the execution.

These kind of files give you a play-by-play of the program and how it behaved, where this will pay off is when you begin to analyze your data and notice that something is kinda off. There are even some programmers that will statically analyze these files for errors or inconsistent patterns, and then give a quality rating to the resulting computed product.

**Debuggers and IDEs**

> A very false sense of security

With the advances in Integrated Development Environments, it has become very easy to rely on their ability to start, stop and inspect your program in real time. It is vitally important to keep in mind that when you rely solely on an IDE or debugger, you can only see into the program at at given point in time, you can not fully verify the full runtime state of the code.
