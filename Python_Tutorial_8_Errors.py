#Syntax Errors
#while True print("hello, world")
#SyntaxError: invalid syntax

#Exceptions
#print(10 *(1/0))
#ZeroDivisionError: division by zero

#print('2' + 2)
#TypeError: can only concatenate str (not "int") to str


#Handling Exceptions
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print('Oops! That was no valid number. Try again...')


#An except clause may name multiple exceptions as a parenthesized tuple
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except (RuntimeError, TabError, NameError):
        #print('Oops! That was no valid number. Try again...')
        pass

#A class in an except clause is compatible with an exception if it is the same class or a base class
#An Except clause listing a derived class is not compatible with a base class.
#If the except clause were reversed, it wouldd have printed B,B,B -- the first matching except clause is triggered.
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


import sys
try:
    with open('brilliant suggestions at work.txt', 'r') as f:
        s = f.readline()
        i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise