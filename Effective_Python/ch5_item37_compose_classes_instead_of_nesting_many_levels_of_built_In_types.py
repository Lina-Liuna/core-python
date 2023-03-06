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
import collections
class BySubjectGradeBook:
    def __init__(self):
        self._grade = {}

    def add_student(self, name):
        self._grade[name] = collections.defaultdict(list)

    def report_grade(self, name, subject, grade):
        by_subject = self._grade[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grade[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

book = BySubjectGradeBook()
book.add_student('Lina Liu')
book.report_grade('Lina Liu', 'math', 100)
book.report_grade('Lina Liu', 'Reading', 90)
book.report_grade('Lina Liu', 'oral english', 80)
book.report_grade('Lina Liu', 'WorkOut', 99)
# print(book._grade)   # inner data with underscore, better not call it outside the class.
print(book.average_grade('Lina Liu'))

# Problem: I want to track the weight of each score toward the overall grade in the class.
# add midterm and final exams and pop quizes.

# Solution: change the innermost dictionary,
# Instead of mapping subjects(its keys) to a list of grades(its values),
# Use the tuple of (score, weight) in the values list:


class WeightGradeBook:
    def __init__(self):
        self._grade = {}

    def add_student(self, name):
        self._grade[name] =collections.defaultdict(list)

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grade[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grade[name]

        score_sum, score_count = 0, 0
        for subject, scores, in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight
            score_sum += subject_avg / total_weight
            score_count += 1

        return score_sum / score_count

book = WeightGradeBook()
book.add_student('Lina')
book.report_grade('Lina', 'Math', 90, 0.3)
book.report_grade('Lina', 'Math', 98, 0.2)
book.report_grade('Lina', 'WorkOut', 90, 0.2)
book.report_grade('Lina', 'WorkOut', 99, 0.3)
print(book.average_grade('Lina'))
