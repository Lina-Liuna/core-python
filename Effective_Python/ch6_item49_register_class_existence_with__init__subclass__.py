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

