# core-python
### 3. Effective Python 
90 Specific ways to write better Python
#### Chapter 1: Pythonic Thinking
##### 1. item 1: know which version of python you're using

##### 2. item 2: follow the PEP 8 style Guide
###### Things to Remember
Always follow the Python Enhancement Proposal #8 (PEP 8) style
guide when writing Python code.

Sharing a common style with the larger Python community facilitates collaboration with others.

Using a consistent style makes it easier to modify your own code later.
##### item 3: Know the difference between bytes and str
###### Things to Remember 
bytes contains sequences of 8-bit values, and str contains sequences of Unicode code points.
Use helper functions to ensure that the inputs you operate on
are the type of character sequence that you expect (8-bit values,
UTF-8-encoded strings, Unicode code points, etc).

bytes and str instances can’t be used together with operators (like>, ==, +, and %).

If you want to read or write binary data to/from a file, always open
the file using a binary mode (like 'rb' or 'wb').

If you want to read or write Unicode data to/from a file, be careful about your system’s default text encoding. Explicitly pass the
encoding parameter to open if you want to avoid surprises.

##### item 4: Prefer interpolated F-Strings over C-style Format strings and str.format
###### Things to Remember
C-style format strings that use the % operator suffer from a variety
of gotchas and verbosity problems.

The str.format method introduces some useful concepts in its formatting specifiers mini language, but it otherwise repeats the mistakes of C-style format strings and should be avoided.

F-strings are a new syntax for formatting values into strings that
solves the biggest problems with C-style format strings.

F-strings are succinct yet powerful because they allow for arbitrary Python expressions to be directly embedded within format
specifiers.
##### item 5: Write helper functions instead of complex expressions
##### item 6: Prefer multiple assignment unpacking over indexing
##### item 7: Prefer enumerate over range
##### item 8: Use zip to process iterators in Parallel
##### item 9: Avoid else blocks after for and while loops
##### item 10: Prevent repetition with assignment expression

### 2. The Python Standard Library

What Pythons's Standard Library Provide?

1. Wide Range of facilities

2. built-in modules(written in C) to access to system functionality such as file I/O

3. Standardized solutions for many problems that occur in everyday programming

4. Modules designed to abstracting away platforms —neutral APIs

5. Provides as a collection of packages, Collections of packages: python package index website
          https://pypi.org/
### 1. Python Tutorial.key & Python Tutorial.pdf is not for presentatioon(there is no graphs and it's not pretty enough, but real useful notes), it's only a note summary.

    python3 this: The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!



