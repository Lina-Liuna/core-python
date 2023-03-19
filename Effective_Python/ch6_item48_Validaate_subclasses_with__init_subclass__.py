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
