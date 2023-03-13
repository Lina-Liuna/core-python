# Every python class is a container encapsulating attributes and functionality together.

# If you are designing classes for simple use cases like sequences, use baseclass from built-in types
# Example: Create my own custom list and counting the frequency of its memebers

class LinaWorkout(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        print(f'self={self}')
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts


workout = LinaWorkout(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Mon', 'Fri', 'Tue', 'Mon'])
print(len(workout))
print(workout.frequency())
workout.pop()
print(repr(workout))
print(workout.frequency())


# How to provide sequence sematics(like list or tuple) for a binary tree class


# collections.abc module defines a set of abstract base classes that provide all of the typical method
# for each container type.
# when you subclass from those abstract base classes and forget to implement required methods,
# the module tells you something is wrong.

import collections.abc

class BadType(collections.abc.Sequence):
    pass

# foo = BadType()  # TypeError: Can't instantiate abstract class BadType with abstract methods __getitem__, __len__

# Example: # How to make binary tree class act like a sequence type?
class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class IndexableNode(BinaryNode):
    def _traverse(self):
        if self.left is not None:
            yield  from self.left._traverse()
        yield self
        if self.right is not None:
            yield from self.right._traverse()

    def __getitem__(self, index):
        for i, item in enumerate(self._traverse()):
            if i == index:
                return item.value
        raise IndexError(f'Index {index} is out of range')


class SequenceNode(IndexableNode):
    def __len__(self):
        max = 0
        for count, _ in enumerate(self._traverse(), 1):
            max = count
            pass
        return max



class TreeNode(SequenceNode, collections.abc.Sequence):
    pass

tree = TreeNode(
    10,
    left=TreeNode(
        5,
        left=TreeNode(2),
        right=TreeNode(
            6,
            right=TreeNode(7))),
    right=TreeNode(
        15,
        left=TreeNode(11))
)

print('Index of 7 is', tree.index(7))
print('count of 10 is', tree.count(10))

# # Things to Remember:
# 1. Inherit directly from pythons' container types( list or dict) for simple use cases
# 2. Beware of the largest number of methods required to implement custom container type correctly.
# 3. Have your custom container types inherit from the interfaces defined in collections.abc to
# ensure that your class match the required interfaces and behaviors.
