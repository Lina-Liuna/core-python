# What is Metaclasses?
# The name metaclass veguely implies a concept above and beyond a class.
# Metaclasses le  you intercept python's class statement and provide special behavior each time class is defined.

# Metaclasses can create extremely bizarre behaviors that are unapproachable to newcomers.
# better to follow the rule of least surprise and only use these mechanisms to implement well understood idioms.

# In python, you never need to implement explicit setter or getter method.
# you should always start your implementations with simple public attributes.

class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

r1 = Resistor(50e3)
r1.ohms = 10e3

r1.ohms += 5e3
print(r1.ohms)

# define a new subclass to vary the current by assigning the voltage property.
# use the @property decorator.
# setter and getter method in subclass.

class VoltageResistence(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._votage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._votage = voltage
        self.current = self._votage / self.ohms

r2 = VoltageResistence(1e3)
print(f'Before: {r2.current:.2f} amps')
r2.voltage = 10
print(f'After:  {r2.current:.2f} amps')


# define a subclass that ensures all resistance values are above zeor ohms
class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'ohms must be > 0; got {ohms}')
        self._ohms = ohms

r3 = BoundedResistance(1e3)
r3.ohms = 0.01

# use the @property to make attributes from parent classes immutable
class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError('Ohms is immutable')
        self._ohms = ohms

r4 = FixedResistance(1e3)
# r4.ohms = 2e3   # AttributeError: Ohms is immutable

# Never set attribute in get method.
# setting other attributes in getter property methods leads to extremely bizarre behavior.

# Other NOTEs:
# avoid :
# 1. importing modules bynamically
# 2. running slow helper functions
# 3. doing I/O
# 4. making expensive database queries

# Expect of using @property:
# 1. quick and easy
# 2. use normal method to do anythong more complex or slow.

# shortcomes of @property:
# 1. the methods of an attribute can only be shared by subclasses.
# unrelated classes can't share the same implementation.
# can use descriptors




