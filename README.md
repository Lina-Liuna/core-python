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
###### things to remember

Things to Remember
Python’s syntax makes it easy to write single-line expressions that are overly complicated and difficult to read.

Move complex expressions into helper functions, especially if you need to use the same logic repeatedly.

An if/else expression provides a more readable alternative to using the Boolean operators or and and in expressions.

##### item 6: Prefer multiple assignment unpacking over indexing
###### things to remember: 
python has special syntax called unpacking for assigning multiple values in a single statement.

unpacking is generalized in python and can be applied to any iterable, including many levels of iterable within 
iterables 

using unpacking to avoid explicitly indexing into sequences.

##### item 7: Prefer enumerate over range
###### things to remember: 
enumerate provides concise syntax for looping over an iterator and getting the index of each 
item from the iterator as you go. 

Prefer enumerate instead of looping over a range and indexing into a sequence

you can supply a second parameter to enumerate to specify the number from which to begin counting(zero is default)

##### item 8: Use zip to process iterators in Parallel
###### things to remember:
the zip func can be used to iterate over multiple iterators in parallel

zip create lazy generator that produces tuples, so it can be used on infinitely long inputs.

zip truncates its output silently to the shortest iterator if you supply it with iterators of different lengths

use the zip_longest function from itertools

##### item 9: Avoid else blocks after for and while loops
###### things to remember:
Avoid using else blocks after loops because their behavior isn't intuitive and can be confusing.

##### item 10: Prevent repetition with assignment expression
###### things to remember: 
Assignment expressions use the walrus operator(:=) to both assign and evaluate variable names 
in a single expression, thus reduce repetition .

when an assignment expression is a subexpression of a larger expression, it must be surrounded with parentheses.

use assignment expression makes code more clearly.

### Ch 2: Lists and Dictionaries
#### item 11: know how to slice sequences
##### things to remember:

avoid being verbose when slicing: don't supply 0 for the start index or the length of the squence for the end index

slicing is forgiving of start and end indexes that are out of bounds

Assigning to a list slice replaces that range in the original sequence

#### item 12: Avoid Striding and Slicing in a single expression
##### Things to remember
specifying start, end, and stride in a slice can be extremely confusing
prefer using positive stride values in slices without start or end indexes. 

avoid negative stride values if possible.

avoid using start, end, and stride together in a single slice.

If you need all three parameters, consider doing two assignments(one to stride and another to slice) or using
is lice from the itertools built-in module.

#### item 13: Prefer Catch-All unpacking Over Slicing

##### Things to Remember: 
Unpacking assignment may use a starred expression to catch all values that weren't assigned to 
the other parts of the unpacking pattern into a list. 

Starred expression may appear in any position, and they will 
always become a list containing the zero or more values they receive. 

when dividing a list into non-overlapping pieces, catch-all unpacking is much less error prone than slicing and 
indexing. 

#### item 14: Sort by Complex Criteria Using the key parameter
##### things to remember:
The sort method of the list type can be used to rearrange list's contents by natural ordering 

the key parameter of the sort method can be used to supply a helper function that returns the value to use 
for sorting in place of each item from the list.

returning a tuple from the key function allows you to combine multiple sorting criteria together.

you can combine many sorting criteria together by calling the sort method multiple times using different key 
functions. 

#### item 15: Be cautious when relying on dict insertion ordering
##### Things to remember:

Since Python 3.7, you can rely on the fact that iterating a dict instances contents will occur in the same order
in which the keys were initially added.

Python makes it easy to define objects that act like dictionaries but that are not dict instances.
For these types, you can't assume that insertion ordering will be preserved.

There are three ways to be careful about dictionary-like classes: 
Write code that doesn't rely on insertion ordering. 
Explicitly check for the dict type at runtime
require dict types using type annotations and static analysis.

#### item 16: Prefer get Over in and KeyError to Handle Missing Dictionary keys
##### Things to remember:

There are four common ways to detect and handle missing keys in dictionary: using in , keyError,
get method, setdefault method

the get method is best for dict that contain basic types like counters, and it is preferable along with assignment 
expressions when creating dictionary values has a high cost or may raise exceptions

when the setdefault method of dict seems like the best fit for your problem, 
you should consider using defaultdict instead

#### item 17: Prefer defaultdict over setdefault to handle missing items in internal state
##### Things to remember:

If you are creating a dictionary to manage an arbitrary set of potential keys, then you should prefer using 
defaultdict instance from the collections

If a dictionary of arbitrary keys is passed to you, and you don't control its creation, then you should prefer 
the get method to access its items. consider using the setdefault methods it leads to short code.

#### item 18: Know how to construct key-dependent default values with __missing__
##### Things to remember:
the setdefault method of dict is a bad fit when creating the default value has high computational cost or 
may raise exceptions.

The function passed to defaultdict must be not require any arguments, which makes it impossible to have he default 
value depend on the key being accessed.

You can define your own dict subclass with a __missing__ method in order to construct default values that must know
which key was being accessed.

### CH 3 Functions
#### item 19: Never Unpack More Than Three Variables When Functions Return Multiple Values
##### Things to remember:

You can have functions return multiple values by putting them in a tuple and having the caller take advantage of 
Pythons' unpacking syntax.

Multiple return values from a function can also be unpacked by catch-all starred expressions.

Unpacking into four or more variables is error prone and should be avoided, instead return a small class or namedtuple instance.

#### item 20: Prefer Raising Exceptions to Returning None
Things to remember:
Functions that return None to indicate special meaning are error prone because None and other values 
Error Prone: zero and empty string all evaluate to False in conditional expressions

Raise exceptions to indicate special situations instead of returning None.

Type annotations can be used to make it clear that a function will never return the value None, even in special situations

#### item 21: Know How Closures Interact with Variable Scope
##### Things to remember:
1. Closure functions can refer to variables from any of the scopes in which they were defined
2. By default, closures can't affect enclosing scopes by assigning variales.
3. Use the nonlocal statement to indicate when a closure can modify a variable in its enclosing scopes
4. Avoid using nonlocal statements for anything beyond simple functions.

#### item 22: Reduce Visual Noise with Variable Positional Arguments
##### Things to remember:
1. Functions can accept a variable number of positional arguments by using *args in the def statement.
2. You can use the items from a sequence as the positional arguments for a function with the * operator.
3. Using the * operator with a generator may cause a program to run out of memory and crash.
4. Adding new positional parameters to functions that accept *args can introduce hard-to-detect bugs.

#### item 23: Provide Optional Behavior with keyword Arguments
##### Things to remember:
1. Function arguments can be specified by position or by keyword
2. keyword make it clear what the purpose of each argument is when it would be confusing with only positional argument.
3. keyword arguments with default values make it easy to add new behaviors to a function without needing to migrate 
all existing calls.
4. Optional keyword arguments should always be passed by keyword instead of by position.

#### item 24: Use None and Docstrings to Specify Dynamic Default Arguments
##### Things to remember:
1. A default argument value is evaluated only once: during function definition at module load time.
This can cause odd behaviors for dynamic values like {}, [], or datetime.now()

2. Use None as the default value for any keyword argument that has a dynamic value.
Document the actual default behavior in the functions docstring.

3. Using None to represent keyword argument default values also works correctly with type annotations.


#### item 25: Enforce Clarity with Keyword-Only and Positional-only Argument
##### Things to remember:
1. Keyword-only arguments force callers to supply certain arguments by keyword (instead of by position), 
which makes the intention of a function call clearer. Keyword-only arguments are defined after a single * in the argument list.

2. Positional-only arguments ensure that callers can’t supply certain parameters using keywords,
which helps reduce coupling. Positional-only arguments are defined before a single / in the argument list.

3. Parameters between the / and * characters in the argument list may be supplied by position or keyword, 
which is the default for Python parameters.

#### item 26: Define Function Decorators with functools.wraps

##### Things to Remember
1. Decorators in Python are syntax to allow one function to modify another function at runtime.
2. Using decorators can cause strange behaviors in tools that do introspection, such as debuggers.
3. Use the wraps decorator from the functools built-in module when you define your own decorators to avoid issues.

#### item 27: Use comprehensions instead of map and filter
##### Things to remember:
1. List comprehensions are clearer than the map and filter built-in functions 
because they don’t require lambda expressions

2. List comprehensions allow you to easily skip items from the input list, 
a behavior that map doesn’t support without help from filter.

3. Dictionaries and sets may also be created using comprehensions.

#### item 28: Avoid more than two control subexpressions in comprehensions
##### Things to Remember
1. Comprehensions support multiple levels of loops and multiple con- ditions per loop level.
2. Comprehensions with more than two control subexpressions are very difficult to read and should be avoided.

#### item 29: Avoid Repeated Work in Comprehensions by Using Assignment Expressions
##### Things to Remember
1. Assignment expressions make it possible for comprehensions and generator expressions 
to reuse the value from one condition else- where in the same comprehension, which can improve readability and performance.

2. Although it’s possible to use an assignment expression outside of a comprehension or 
generator expression’s condition, you should avoid doing so.

#### item 30: Consider Generators instead of returning lists
##### Things to remember:
1. using generators can be clearer than the alternative of having a function return a list of accumulated results.
2. the iterator returned by a generator produces the set of values passed to yield expressions within the generator 
function's body.
3. Generators can produce a sequence of outputs for arbitrarily large inputs because their working memory doesn't 
include all inputs and outputs.

#### item 31: Be defensive when iterating over arguments
##### Things to remember:
1. Beware of functions and methods that iterator over input arguments multiple times.
If these arguments are iterators, you may see strange behavior and missing values.

2. Python's iterator protocol defines how containers and iterator interact with the iter and next built-in functions,
for loops, and related expressions.

3. You can easily define your own iterable container type by implementing the __iter__ method as a generator.

4. You can detect that a value is an iterator(instead of a container) if calling iter on it produces the same value
as what you passed in. Alternatively, you can use the isinstance built-in function
along with the collections.abc.Iterator class.

#### item 32: Consider Generator expressions for large list comprehensions.
##### Things to Remember:
1. List comprehensions can cause problems for large inputs by using too much memory
2. Generator expressions avoid memory issues by producing outputs one at a time as iterators.
3. Generator expressions can be composed by passing the iterator from one generator expression 
into the for subexpression of another.
4. Generator expressions execute very quickly when chained together and are memory efficient.


#### item 33: Compose Multiple Generators with yield from
##### Things to Remember
1. the yield from expression allows you to compose multiple nested generators together into a single combined generator.
2. yield from provides better performance than manually itertating nested generators and yielding their outputs.


#### item34: Avoid injecting data into generators with send
##### Things to Remember
1. The send method can be used to inject data into a generator by giving the yield expression a value that can be 
assigned to a variable.

2. Using send with yield from expressions may cause surprising behavior, such as non values appearing at unexpected times 
in the generator output

3. Providing an input iterator to a set of composed generators is a better approach than using send method,
which should be avoided.

#### item35: Avoid Causing State Transitions in Generators with throw.
##### Things to Remember:

1. The throw method can be used to re-raise exceptions within generators at the position of the most recently 
executed yield expression

2. using throw harms readability because it requires addtional nesting and boilerplate in order to raise and catch 
exceptions

3. A better way to provide exceptional behavior in generator is to use a class that implements the __iter__ method
along with method to cause exceptional state transitions.

#### item36: Consider itertools for working with iterators and generators
##### Things to Remember:
1. The itertools functions fall into three main categories for working with iterators and generators:
   1. linking iterators together
   2. filtering items they output
   3. producing combinations of items
2. There are more advanced functions, additional parameters, and useful recipe available in the help(itertools)

### 2. The Python Standard Library

What Pythons's Standard Library Provide?

1. Wide Range of facilities

2. built-in modules(written in C) to access to system functionality such as file I/O

3. Standardized solutions for many problems that occur in everyday programming

4. Modules designed to abstracting away platforms —neutral APIs

5. Provides as a collection of packages, Collections of packages: python package index website
          https://pypi.org/
### 1. Python Tutorial
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

# The following two lines: resolve ssl SSL: CERTIFICATE_VERIFY_FAILED problem
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



