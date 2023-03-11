# What if you want multiple inheritance, but want to avoid the potential headaches? writing a mix-in instead.

# what is mix-in class?
# A mix-in class is a class that defines only a small set of additional methods for its child classes to provide.
# mix-in class don't define instance attributes and __init__ constructor.

# python make mix-in to inspect the current state of any object, regardless of its type.

# What does dynamic inspection mean?
# Dynamic inspection means you can write generic functionlaity just once, in a mix-in, and it can then be applied
# to many other classes.

class ToDictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value

class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = BinaryTree(10,
    left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, left=BinaryTree(11)))
print(tree.to_dict())


# what the best part about mix-ins is that you can make their generic functionality pluggable
# so behaviors can be overridden when required.


# define a subclass of BinaryTree that holds a reference to its parent.
class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent

    def _traverse(self, key, value):
        if (isinstance(value, BinaryTreeWithParent) and
                key == 'parent'):
            return value.value    # Prevent cycles
        else:
            return super()._traverse(key, value)

root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
print(root.to_dict())





