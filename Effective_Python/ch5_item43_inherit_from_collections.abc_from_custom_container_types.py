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