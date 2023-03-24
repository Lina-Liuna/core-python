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


# Problem: in Customer class: fist_name property redundant with string first_name
# Questions: How to solve the  class property redundant problem?
# Reason why: first the constuctor is called as Field('first_name),
            # Second, the return value of that is assigned to Customer.field_name
            # third, the return vlaue of that is assigned to Customer.field_name.
            # There is no way for a Field instance to know upfront which class attribute it will be assigned to.
# SOlution: metaclass

# Metaclass let you hook the class statement directly and take action as soon as a class body is finished.
# use the metaclass to assign Field.name and Field.internal_name on the descriptor automatically
# instead of manually specifying the field name multiple times.

class Field:
    def __init__(self):
        # These will be assigned by the metaclass
        self.name = None
        self.internal_name = None

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


class DatabaseRow(metaclass=Meta):
    pass


class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
suffix = Field()

cust = BetterCustomer()
print(f'Before: {cust.first_name!r} {cust.__dict__}')
cust.first_name = 'LinaLLLLLL'
print(f'After: {cust.first_name!r} {cust.__dict__}')


# Problem: DatabaseRow seems no good, how to remove it without error?
# Solution: use __set_name__(self, owner, name)
class Field:
    def __init__(self):
        self.name = None
        self.internal_name = None

    def __set_name__(self, owner, name):
        # Called on class Creation for each descriptor
        self.name = name
        self.internal_name = '_' + name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class FixedCustomer:
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()

cust = FixedCustomer()
print(f'Before:{cust.first_name!r} {cust.__dict__}')
cust.first_name = 'LINAAAA'
print(f'After:{cust.first_name!r} {cust.__dict__}')
