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