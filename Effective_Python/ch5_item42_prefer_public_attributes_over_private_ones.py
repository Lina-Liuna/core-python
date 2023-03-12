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


