# what is Python hooks:
# hooks write generic code for gluing systems together.

# Example: represent the records in a database as Python objects.

# should we know what the database looklike before represent them?
# needn't to, it can be generic.

# How do this?
# plain instance attributes, @property methods and descriptors can't to this.
# Why?
# they need to be defined in advance.

# Python advanced feature:
# dynamic behavior: with __getattr__ method.

# __getattr__ method called everytime an attribute can't found in an object's instance dictionary.


class LazyRecord:
    def __init__(self):
        self.exists = 5
    def __getattr__(self, name):
        value = f'Value for {name}'
        setattr(self, name, value)
        return value

data = LazyRecord()
print('Before:', data.__dict__)
print('foo:   ', data.foo)
print('After: ', data.__dict__)