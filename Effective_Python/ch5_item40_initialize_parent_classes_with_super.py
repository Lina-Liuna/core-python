# how to initialize a parent class from a child class?
# simple way directly call the parent class's __init__method with the child instance.

class LinaShoe:
    def __init__(self, size):
        self.size = size

class LinaLeftShoe:
    def __init__(self):
        LinaShoe.__init__(self, 7)


# THe above only works fine for basic class hirearchies but breaks in many cases.
# if multiple inheritance calling the superclass __init__ method directly can lead to unpredictable behavior.
