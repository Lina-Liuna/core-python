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


CalcNum = CalcNumers(7)
print('7 * 2 + 5 = ', CalcNum.value)

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


CalcNum = CalcNumers_different_orders(7)
print('7 * 2 + 5 = ', CalcNum.value)

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

CalcNum = CalcNumber(5)
print('should be 5 * 2 + 5 = 15 but is:', CalcNum.value)

# The Problem above is: PlusFive.__init__ causes self.value to be reset back to 5 when BaseNumber.__init__ get called
# a second time.

# This behavior is surprising and can be very difficult to debug in more complex cases.
























