# Advanced metaclass: automatically register types in a program
# Registration is useful for doing reverse lookups.
# you need to map a simple identifier back to a corresponding class.

# Example: I want to implement my own serialized representaion of a Python object using JSON.
# Need a way to turn a object into a JSON string.
import json


class Serializable:
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args': self.args})


class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'


point = Point2D(5, 3)
print('Object:    ', point)
print('Serialized:', point.serialize())

# Deserialize the JSON string and construct the Point2D object it represents.
# define a class that can deserialize the data from its Serializable parent class:


class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])

class Point2D(Deserializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'

before = Point2D(5, 3)
print('Before:    ', before)
data = before.serialize()
print('Serialized:', data)
after = Point2D.deserialize(data)
print('After:     ', after)

# Problem: the above code only works if you know the intended type of the serialized data
# ahead of time.

# Ideal Condition:
# A large number of classes serializing to JSON and one common function that could
# deserialize any of them back to a corresponding Python object.

# Include the serialized object's class name in the JSON data.

class Serializable:
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args,
        })

    def __repr__(self):
        name = self.__class__.__name__
        arg_str = ','.join(str(x) for x in self.args)
        return f'{name}({arg_str})'

# Then maintain a mapping of class names back to constructors for those objects.
# The general deserialize function works for any classes passed to register_class.


registry = {}

def register_class(target_class):
    registry[target_class.__name__] = target_class

def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

register_class(Point2D)

before = Point2D(5, 3)
print('Before:    ', before)
data = before.serialize()
print('Serialized:', data)
after = deserialize(data)
print('After:     ', after)


# Problem: Must Reister_class first, to store class name inside registry dictionary
# Solution: Use metaclasses to intercepting the class statement when subclasses are defined.
# Example: Use a metaclass to register the new type immediately after the class's body.


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls

class RegisteredSerializable(Serializable, metaclass=Meta):
    pass

class Vector3D(RegisteredSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x, self.y, self.z = x, y, z

before = Vector3D(10, -7, 3)
print('Before:    ', before)
data = before.serialize()
print('Serialized:', data)
print('After:     ', deserialize(data))

# Finally solution: use __init_subclass__ special method


class RegisteredSerializable(Serializable):
    def __init_subclass__(cls):
        super().__init_subclass__()
        register_class(cls)


class Vector1D(RegisteredSerializable):
    def __init__(self, magnitude):
        super().__init__(magnitude)
        self.magnitude = magnitude

before = Vector1D(6)
print('Before:    ', before)
data = before.serialize()
print('Serialized:', data)
print('After:     ', deserialize(data))


# use __init_subclass__ for class registration, you can ensure you'll never miss registering a class
# this works for:
# 1. serialization,
# 2. database object-relational mappings(ORMs),
# 3. extensible plug-in system
# 4. callback hooks

