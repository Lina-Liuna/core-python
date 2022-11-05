#An Example demonstrating how to reference the different scopes and namespaces
#How global and nonlocal affect variable binding:
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'

    def do_global():
        global spam
        spam = 'global spam'

    spam = 'test spam'
    do_local()
    print('After local assignment:', spam)
    do_nonlocal()
    print('After nonlocal assignment:', spam)
    do_global()
    print('After global assignment:', spam)

scope_test()
print('In global scope:', spam)

#class may define __init__() to specific initial state
#when a class defines an __init__()method, class instantiation automatically invokes __init__() for the newly created class instance.
#__init__() may have arguments for greater flexibility.
#arguments given to the class instantiation operator are passed on to __init__()
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def f(self):
        print('hellow world!')

x = Complex(3.0, -4.5)
print(x.r, x.i)
xf = x.f
while True:
    print(xf())