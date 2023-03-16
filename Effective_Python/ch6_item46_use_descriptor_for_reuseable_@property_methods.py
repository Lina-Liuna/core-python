# What's the problem of @property?
# @property methods it decorates can't be reused for multiple attributes of the same class.
# @property methods it decorates can't be reused by unrelated classes.

# Example:
# I want a class to validate that the grade received by a student on a homework assignment is a percentage.

# Example to explian: what is the side effect of @property? why we use descriptor instead
class Homework:
    def __init__(self):
        self._grade = 0
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError(
                'Grade must be between 0 and 100')
        self._grade = value

class Exam:
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0
    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError(
                'Grade must be between 0 and 100')

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value


Lina = Homework()
Lina.grade = 100
print(Lina.grade)

Lina = Exam()
Lina.math_grade = 99
Lina.writing_grade = 88
print(Lina.math_grade, Lina.writing_grade)

# The problem of above code:
# If I want to reuse this percentage validation in other classes beyond homework and exams,
# I will need to write the @property boilerplate and _check_grade method over and over again.

# How to solve this?
# Use the descriptor in python
# What is descriptor?
# descriptor is a protocol defines how attribute access is interpreted by the language.

# A descriptor can provide __get__ and __set__ methods that let you reuse the grade validation behavior
# without boilerplate.
# descriptor is also better than mix-ins.

# descriptor allows you to reuse the same logic for many different attributes in a single class.


class Grade:
    def __init__(self):
        self._value = 0
    def __get__(self, instance, instance_type):
        return self._value
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError(
                'Grade must be between 0 and 100')
        self._value = value


class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

LinaExam = Exam()
LinaExam.writing_grade = 82
LinaExam.science_grade = 99
print('Writing', LinaExam.writing_grade)
print('Science', LinaExam.science_grade)

NanaExam = Exam()
NanaExam.writing_grade = 77
print('Nana Writing', NanaExam.writing_grade)
print('Lina Writing', LinaExam.writing_grade)

# How to above access multi-attributes on multiple exam instances causes unexpected behavior?
# Solution:
# Keep track of its value for each unique exam instance.
# Saving the per-instance state in a dictionary.
class Grade:
    def __init__(self):
        self._values = {}
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError(
                'Grade must be between 0 and 100')
        self._values[instance] = value

class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

LinaExam = Exam()
LinaExam.writing_grade = 82
LinaExam.science_grade = 99
print('Writing', LinaExam.writing_grade)
print('Science', LinaExam.science_grade)

NanaExam = Exam()
NanaExam.writing_grade = 77
print('Nana Writing', NanaExam.writing_grade)
print('Lina Writing', LinaExam.writing_grade)

# The above code works well, but still one gotcha: it leaks memory.
# The _values dictionary holds a reference to every instance of Exam ever passed to __set__
# over the lifetime of the program. This causes instances to never have their reference count go to zero,
# preventing cleanup by the garbage collector

# How to fix the leak memory problem?
# Solution: use weakref built-in module
# weakref provides a special class called WeakKeyDictionary that can take the place of the imple dictionary
# used for _values.

# The unique behavior of WeakKeyDictionary is that
# the WeakKeyDictionary removes Exam instances from its set of items
# when the Python runtime knows it’s holding the instance’s last remaining reference in the program.
# Python does the bookkeeping for me and ensures that the _values dictionary will be empty
# when all Exam instances are no longer in use:


from weakref import WeakKeyDictionary
class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError(
                'Grade must be between 0 and 100')
        self._values[instance] = value

class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

LinaExam = Exam()
LinaExam.writing_grade = 82
LinaExam.science_grade = 99
print('Writing', LinaExam.writing_grade)
print('Science', LinaExam.science_grade)

NanaExam = Exam()
NanaExam.writing_grade = 77
print('Nana Writing', NanaExam.writing_grade)
print('Lina Writing', LinaExam.writing_grade)


# Things-to-Remember:
# 1. Reuse the behavior and validation of @property methods by defining your own descriptor classes.
# 2. Use WeakKeyDictionary to ensure that your descriptor classes don’t cause memory leaks.
# 3. Don’t get bogged down trying to understand exactly
# how __getattribute__ uses the descriptor protocol for getting and set- ting attributes.