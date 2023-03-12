# In python there are two types of visibility for a class's attributes:
# public and private

class LinaGit:
    def __init__(self):
        self.public_repositories = 12
        self.__private_repo = 4

    def get_private_repo(self):
        return self.__private_repo

    # class method have access to private attributes because they are declared within the surrounding class block.
    @classmethod
    def get_private_repo_of_instance(cls, instance):
        return instance.__private_repo

lngit = LinaGit()
assert lngit.public_repositories == 12
assert lngit.get_private_repo() == 4
assert LinaGit.get_private_repo_of_instance(lngit) == 4
# print(lngit.__private_repo)  # Error

# A subclass can't access its parent class's private fields:
class LinaGitChild(LinaGit):
    def get_private_repo(self):
        return self.__private_repo

lngitchild = LinaGitChild()
# lngitchild.get_private_repo()  #Error:

# How to access private attributes of any class- from a subclass or externally--without asking permission
print(lngitchild._LinaGit__private_repo)

# look in the object's attribute dictionary, you can see the private attribute are actually stored with
# the named as they appear after the tranformation.
print(lngitchild.__dict__)

# if you insisted call private attribute, once the class hierarchy changes beneath you, these classes will
# break because the private attribute references are no longer valid.

# better ways:
# Document each protected field and explain which fields are internal API available to subclasses and
# which should be left alone entirely.


# The only time to seriously consider using private attributes is when you're worried about naming conflicts
# with subclasses.

# This problem occurs when a child class unwittingly defines an attribute that was already defined
# by its parent class.

# To reduce the risk of this issue occuring, you can use a private attribute in the parent class
# to ensure that there are no attribute names that overlap with child classes.

class BaseClass:
    def __init__(self):
        self.__value = 5

    def get(self):
        return self.__value

class ChildClass(BaseClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'

a = ChildClass()
print(f'{a.get()} and {a._value} are differnt')

# Things-to-Remember:
#1. Private attributes aren't rigorously enforced by the Python compiler

# 2. Plan from the beginning to allow subclasses to do more with your internal APIs and attributes
# instead of choosing to lock them out

# 3. Use documentation of protected fields to guide subclasses instead of trying to force access control
# with private attributes

# 4. Only consider using private attribute to avoid naming conflicts with subclasses that are out of your control
