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

class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(f'* Called __getattr__({name!r}), '
              f'populating instance dictionary')
        result = super().__getattr__(name)
        print(f'* Returning {result!r}')
        return result
data = LoggingLazyRecord()
print('exists:     ', data.exists)
print('First foo:  ', data.foo)
print('Second foo: ', data.foo)

# Example :
# I want to transactions in this database system.
# The next time the user accesses a property, I want to know whether the corresponding record in the database
# is still valid and whether the transaction is still open.

# Solution:
# object hook: __getttribute__
# __getattribute__ called every time an attribute is accessed on an object
# We can do things like check global transaction state on every property access.
# side effect of using __getattribute__:
# using __getattribute__ can incur significant overhead and negatively impact performance.

class ValidatingRecord:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print(f'Called __getattribute__({name!r})')
        try:
            value = super().__getattribute__(name)
            print(f'Found {name!r}, returning {value!r}')
            return value
        except AttributeError:
            value = f'Value for {name}'
            print(f'Setting {name!r} to {value!r}')
            setattr(self, name, value)
            return value


data = ValidatingRecord()
print('exists: ', data.exists)
print('first foo: ', data.foo)
print('second foo', data.foo)


# hasattr built-in function to determine when properties exists
# getattr built-in function to retrieve property values.


data = LoggingLazyRecord()  # Implements __getattr__
print('Before:         ', data.__dict__)
print('Has first foo:  ', hasattr(data, 'foo'))
print('After:          ', data.__dict__)
print('Has second foo: ', hasattr(data, 'foo'))

data = ValidatingRecord()  # Implements __getattribute__
print('Has first foo:  ', hasattr(data, 'foo'))
print('Has second foo: ', hasattr(data, 'foo'))

