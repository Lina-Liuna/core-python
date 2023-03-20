# metaclass validation:
# 1. the style
# 2. overriding methods
# 3. have strict relationships between class attributes
# 4. validation code runs in the __init__ method
# 5. Use metaclasses for validation can raise errors much earier.


# what is a metaclass?
# 1. a metaclass is defined by inheriting from type
# 2. a metaclass receives the contents of associated class statements in its __new__method.

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(f'* Running {meta}.__new for {name}')
        print('bases:', bases)
        print(class_dict)
        return type.__new__(meta, name, bases, class_dict)

class MyClass(metaclass=Meta):
    stuff = 123

    def validateinfo(self):
        pass

class MySubclass(MyClass):
    time = 5

    def goodmorning(self):
        pass


# The __new__ in meta will validate all of the parameters of an associated class before its defined!

# Exmple:
# I want to represent any type of multisided polygen.
# I can do this by defining a special validating metaclass and using it in the base class of my polygon class
# hierarchy.


class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # Only validate subclasses of the Polygon class
        if bases:
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)


class Polygon(metaclass=ValidatePolygon):
    sides = None  # Must be specified by subclasses
    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3


class Rectangle(Polygon):
    sides = 4


class Nonagon(Polygon):
    sides = 9

print(Triangle.interior_angles() == 180)
print(Rectangle.interior_angles())
print(Nonagon.interior_angles())

# Error example to validate the validating happened when defining the subclass.
"""
print("before error example")
class Line(Polygon):
    print("before define sides")
    sides = 2
    print('after define sides')
print('after class')
"""

# Advanced feature: __init_subclass__ to validating to avoid metaclass entirely

class BetterPolygon:

    # sides must be specified by subclasses
    sides = None

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError("Polygon need 3+ sides")

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180

class Hexagon(BetterPolygon):
    sides = 6

print(Hexagon.interior_angles())


# Problems when using metaclass to validating subclass:
# You can only specify a single metaclass per class definition
# Error happens: if I define a second metaclass to validating the fill color used for a region.
class ValidateFilled(type):
    def __new__(meta, name, bases, class_dict):
        # Only validate subclasses of the Filled class
        if bases:
            if class_dict['color'] not in ('red', 'green'):
                raise ValueError('Fill color must be supported')
        return type.__new__(meta, name, bases, class_dict)


class Filled(metaclass=ValidateFilled):
    color = None  # Must be specified by subclasses

# class RedPentagon(Filled, Polygon):
    # color = 'red'
    # sides = 5   # Error happened here for multi-metaclass validating


# IF I use __init_subclass__ not such error happens
class Filled:
    color = None  # Must be specified by subclasses
    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.color not in ('red', 'green', 'blue'):
            raise ValueError('Fills need a valid color')

class BetterPolygon:
    # sides must be specified by subclasses
    sides = None
    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError("Polygon need 3+ sides")

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class RedTriangle(Filled, Polygon):
    color = 'red'
    sides = 3

ruddy = RedTriangle()
assert isinstance(ruddy, Filled)
assert isinstance(ruddy, Polygon)