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







