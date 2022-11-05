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
for i in range(0, 10):
    xf()

class Dog:
    kind = 'canine'    #class variable shared by all instances of the class.

    def __init__(self, name):
        self.name = name #instance variables are for data unique to each instance.

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind, e.kind)     #class variable shared by all dogs
print(d.name, e.name)     #instance variables unique to the specific instance.

#Shared variables in class can be tricky, if shared variables type is list or dictionary
class Dog:

    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)  #class variables unexpectedly shared by all dogs!!!!!

#Correct design of the class should use an instance variable instead:
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []   #creates a new empty list for each dog


    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks)


#what happened if the same attribute name occurs in both an instance and in a class?
#attribute lookup prioritizes the instance.
class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.region, w2.purpose)