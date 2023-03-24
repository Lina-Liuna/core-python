# metaclasses: useful-features: ability to modify or annotate properties after a class is defined but before
# the class is actually used.

#metaclass modify/annotate properties after a class defined but before it used to give more introspection
# into how properties are being used within their containing class.

# Example: define a new class that represents a row in a customer database.
# How to: have a corresponding property on the class for each column in the database table.
# Dedicated: define a descriptor class to connect attributes to column names.

class Field:
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


# With the column name stored in the Field descriptor, I can save all of the per-instance state directly
# then I can load state with getattr

class Customer:
    # Class attributes:
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')

cust = Customer()
print(f'Before:{cust.first_name!r} {cust.__dict__}')
cust.first_name = 'Lina'
print(f'After:{cust.first_name!r}{cust.__dict__}')


