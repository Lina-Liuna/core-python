# object-oriented programming language: inheritance, polymorphism, and encapsulation.
# python class: defining how classes interact through interfaces and hierarchies.

# Dynamic:
# how to maintaining dynamic iternal state?
# pythons's dictionary type is wonderful for maintaining dynamic interal state over the lifetime of an object.

# what is dynamic?
# dynamic is a situation which you need to do bookkeeping for an unexpected set of identifiers.

# Example:
# Record the grades of a set of students whose names arent known in advance.
# Can define a class to store the namex in a dictionary instead of using a predefined attribute for each student.

class SimpleGradeBook:
    def __init__(self):
        self._grade = {}

    def add_student(self, name):
        self._grade[name] = []

    def report_grade(self, name, score):
        self._grade[name].append(score)

    def averae_grade(self, name):
        grades = self._grade[name]
        return sum(grades) / len(grades)

book = SimpleGradeBook()
book.add_student('Lina Liu')
book.report_grade('Lina Liu', 100)
book.report_grade('Lina Liu', 99)
book.report_grade('Lina Liu', 77)
print(book.averae_grade('Lina Liu'))


# problems:
# dictionary is easy to use that there's a danger of overextending them to write brittle code.
# if I want to extend the SimpleGradeBook class to keep a list of grades by subject, not just overall.
# I can change the _grades dictionary to map student names to another dictionary
