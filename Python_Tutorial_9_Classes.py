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

#Assigning a function object to a local variable in the class is ok
def f1(self, x, y):
    return min(x, x+y)

#f, g and h are all attributes of class C that refer to function objects,
#f, g and h are all methods of instances of C
#this is bad practice however
class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

tc = C()
print(tc.h())
print(tc.f(1, 3))

#Methods may call other methods by using method attributes of the self argument
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self,x):
        self.add(x)
        self.add(x)

b = Bag()
b.addtwice(5)
print(b.data)

#name mangling, Any identifier of the form __spam(at least two leading underscores) is textually replaced with _classname__spam
#the mangling is done without regard to the syntactic position of the identifier
#Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls.
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)


    __update = update      #private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        #provides new signature for update() but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)



#python's data type similar to C 'struct', bunding together a few named data items
#An empty class definition
class Employee:
    pass

john = Employee()    #Create an empty employee record

#Fill the fields of the record
john.name = 'John Doe'
john.dept = 'Computer lab'
john.salary = 2000

print(john.name)








