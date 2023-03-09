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


# build and connect the object with some helper functions

# list the contents of a directory and construct a PathInputData instance for each file it contains.
import os

def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield  PathInputData(os.path.join(data_dir, name))


# Create the LineCountWorker instances by using the InputData instances returned by generate_inputs:
def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers

# Execute those worker instances by fanning out the map step to multiple threads,
# Call reduce repeatedly to combine the results into one final value.
from threading import Thread

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result


# connect all the pieces together in a function to run each step:
def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)

# Running this function on a set of test input files works great:
import os
import random

def write_test_files(tmpdir):
    if not os.path.exists(tmpdir):
        os.makedirs(tmpdir)
    for i in range(100):
        with open(os.path.join(tmpdir, str(i)), 'w') as f:
            f.write('\n' * random.randint(0, 100))


tmpdir = 'test_inputs'
write_test_files(tmpdir)

# result = mapreduce(tmpdir)
# print(f'There are {result} lines')

# Problem: mapreduce function is not generic at all.
# If write another InputData or Worker subclass, I would also have to rewrite the genrate_inputs, create_workers,
# and mapreduce functions to match.

# Problem discussion: need a generic way to construct objects.
# constructor polymorphism, requiring that each InputData subclass provide a special constructor
# that can be used generically by the helper methods that orchestrate the MapReduce.

# Python only allows for the single constructor method __init__.
# It is unreasonable to require every InputData subclass to have a compatible constructor.

# Solution: define class method polymorphism
# class method polymorphism for whole classes instead of their constructed objects.

# extend the InputData Class with a generic @classmethod that's responsible for creating new InputData instances
# using a common interface:


class GenericInputData:
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError

class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        with open(self.path) as f:
            return f.read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers

class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result

def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

config = {'data_dir': tmpdir}
result = mapreduce(LineCountWorker, PathInputData, config)
print(f'There are {result} lines')


# Things-to-Remember:
# 1. Python only support a single constructor per class: the __init__ method
# 2. Use @classmethod to define alternative constructors for your classes.
# 3. Use class method polymorphism to provide generic ways to build and connect many concrete subclasses.









