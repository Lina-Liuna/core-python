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

#else clause after try excpet
for arg in sys.argv[1:]:
    try:
        f= open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

#Exception arguments strored in instance.args inside exception instance
#sometimes, instance defines __str__(), so the arguments printed directrly without having args
#sometimes instantiate an exception first before raising it and add any attributes to it as desired.
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))     #The exception instance
    print(inst.args)      #arguments stored in .args
    print(inst)           #__str__ allows args to be printed directly, but maybe overridden in exception subclasses

    x, y = inst.args      #unpack args
    print('x=', x)
    print('y=', y)

#Exception handlers handle exceptions both in try clause and inside functions taht are called in the try clause
def this_fials():
    x = 1/0

try:
    this_fials()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

#use the finally clause to do clean-up actions
def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())

#use the finally clause to do clean-up actions
def devide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is:', result)
    finally:
        print('executing finally clause')

devide(1, 2)
devide(1, 0)
devide("1", "2")

#option finally clause used in try statement to define clean-up actions that must be exectuted under all circumstances
try:
    raise  KeyboardInterrupt
finally:
    print('Goodbye, world!')

#allow raise statement use optional from clause to indicate that an exception is a direct consequnce of another
#using from None allows disabling automatic exception chaining
try:
    open('database.sqlite')
except OSError:
    raise  RuntimeError from None


#allow raise statement use optional from clause to indicate that an exception is a direct consequnce of another
#Useful when you are transforming exceptions
def func():
    raise ConnectionError
try:
    func()
except ConnectionError as exec:
    raise RuntimeError('Failed to open database') from exec

#if an unhandled exception occurs inside an except section, it will have the exception being handled
#attached to it and inclued in the error message
try:
    open('database.squlite')
except OSError:
    raise RuntimeError("unable to handle error")

#to indicate that an exception is a direct consequence of another, the raise statement allows an optional from clause
#exec must be exception instance or None.
raise RuntimeError from exec

#If you need to determine whether an exception was raised but don't intend to handle it,
#a simpiler of the raise statement allows you to re-raise the exception
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by')
    raise