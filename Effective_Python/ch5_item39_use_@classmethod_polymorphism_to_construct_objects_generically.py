# Polymorphism in python:
# object support polymorphism
# classes support polymorphism
# polymorphism enables multiple classes in a hierarchy to implement their own unique versions of a method
# polymorphism means that many classes can fulfill the same interface or abstract base class while providing different
# functionality.

# Example:
# Writing a MapReduce implementation, want a common class to represent the input data.
# Define a class with a read method that must be defined by subclasses:
class InputData:
    def read(self):
        raise NotImplementedError

# concrete subclass of InputData that reads data from a file on disk
class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        with open(self.path) as f:
            return f.read()


class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


# define a concrete subclass of Worker to implement the specific MapReduce function

class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result



