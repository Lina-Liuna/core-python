# how to initialize a parent class from a child class?
# simple way directly call the parent class's __init__method with the child instance.

class LinaShoe:
    def __init__(self, size):
        self.size = size

class LinaLeftShoe:
    def __init__(self):
        LinaShoe.__init__(self, 7)


# THe above only works fine for basic class hirearchies but breaks in many cases.
# if multiple inheritance calling the superclass __init__ method directly can lead to unpredictable behavior.


# Problem: the __init__ call order isn't specified across all subclasses.
# Define two parent classes that operate on the instance's value field.
class BaseNumber:
    def __init__(self, value):
        print('BaseNumber')
        self.value = value

class TimesTwo:
    def __init__(self):
        self.value *= 2

class PlusFive:
    def __init__(self):
        self.value += 5


class CalcNumers(BaseNumber, TimesTwo, PlusFive):
    def __init__(self, value):
        BaseNumber.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


# CalcNum = CalcNumers(7)
# print('7 * 2 + 5 = ', CalcNum.value)

# defines the same parent class but in a different order
# PlusFive followed by TimesTwo
# but the call inside __init__ in the same order as before
# this class's behavior doesn't match the order of the parent classes in its definition.
# the inheritance base classes and the __init__ calls is hard to spot.
class CalcNumers_different_orders(BaseNumber, PlusFive, TimesTwo):
    def __init__(self, value):
        BaseNumber.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


# CalcNum = CalcNumers_different_orders(7)
# print('7 * 2 + 5 = ', CalcNum.value)

# Diamond inheritance:
# Diamond inheritance happens when a subclass inherits from two separate classes that have the same superclass
# somewhere in the hierarchy.

# Diamond inheritance causes the common superclass's __init__ method to run multiple times, causing unexpected behavior.

class TimesTwo(BaseNumber):
    def __init__(self, value):
        BaseNumber.__init__(self, value)
        self.value *= 2

class PlusFive(BaseNumber):
    def __init__(self, value):
        BaseNumber.__init__(self, value)
        self.value += 5

class CalcNumber(TimesTwo, PlusFive):
    def __init__(self, value):
        TimesTwo.__init__(self, value)
        PlusFive.__init__(self, value)

# CalcNum = CalcNumber(5)
# print('should be 5 * 2 + 5 = 15 but is:', CalcNum.value)

# The Problem above is: PlusFive.__init__ causes self.value to be reset back to 5 when BaseNumber.__init__ get called
# a second time.

# This behavior is surprising and can be very difficult to debug in more complex cases.

# How to solve the diamond inheritance problem?
# super built-in function and standard method resolution order(MRO)
# super.__init__ ensures that common superclasses in diamond hierarchies are run only once.
# The standard method resolution order(MRO) defines the ordering in which superclasses are initialized, following
# an algorithm called C3 linearization

class TimesTwo(BaseNumber):
    def __init__(self, value):
        super().__init__(value)
        print('TimesTwo')
        self.value *= 2

class PlusFive(BaseNumber):
    def __init__(self, value):
        super().__init__(value)
        print('PlusFive')
        self.value += 5

class CalcNumber(TimesTwo, PlusFive):
    def __init__(self, value):
        super().__init__(value)

CalcNum = CalcNumber(5)
print(f'should be (5 + 5) * 2 = 20 and is:',CalcNum.value)
'''
class CalcNumber(PlusFive, TimesTwo):
    def __init__(self, value):
        super().__init__(value)
'''


#CalcNum = CalcNumber(5)
#print(f'should be 5 * 2 + 5 = 15 and is:',CalcNum.value)

# MRO
class A:
    def __init__(self):
        print(" In class A")


class B(A):
    def __init__(self):
        super().__init__()
        print(" In class B")


class C(A):
    def __init__(self):
        super().__init__()
        print("In class C")


# classes ordering
class D(B, C):
    pass


r = D()

# Question: shouldn't B.__init__ or TimesTwo.__init__ run first?
# The MRO order

# The MRO ordering is available on a class method called mro
# repr function return the canonical string repreentation of the object
mro_str = '\n'.join(repr(cls) for cls in CalcNumber.mro())
print(mro_str)

# The super functions
# The super function can also be called with two parameters:
# first the type of the class whose MRO parent view you're trying to access.
# second parameters is the instance on which to access that view.

class ExplicitTrisect(BaseNumber):
    def __init__(self, value):
        super(ExplicitTrisect, self).__init__(value)
        self.value /= 3


class AutomaticTrisect(BaseNumber):
    def __init__(self, value):
        super(__class__, self).__init__(value)
        self.value /= 3


class ImplicitTrisect(BaseNumber):
    def __init__(self, value):
        super().__init__(value)
        self.value /= 3


print(ExplicitTrisect(9).value)
print(AutomaticTrisect(9).value)
print(ImplicitTrisect(9).value)

# The only time you should provide parameters to super is in situations where you need to access the specific
# functionality of a super class's implementation from a child class.


# Things-to-Remember:
# 1. Python's standard method resolution order(MRO) solves the problems of superclass initialization
# and diamond inheritance.

# 2. Use the super built-in function with zero arguments to initialize parent classes.




















