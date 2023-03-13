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



