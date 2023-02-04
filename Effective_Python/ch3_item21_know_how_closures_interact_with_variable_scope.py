# What problem to solve?
# I want to sort a list of numbers but prioritize one group of numbers to come first.
# why I want to solve this problem?
# This pattern is useful when you're rendering a user interface and want important messages or exceptional event
# to display before everything else.

# How to solve prioritize one group of numbers to come first when sort a list?
# A common way:
# pass a helper function as the key argument to a list's sort method.
# the helper's return value will be used as the value for sorting each item in the list.
# the helper can check whether the given item is the important group and can vary the sorting value accordingly.

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


numbers = [5,3,6,8,9,0,2]
group = {3,8,9,6}
sort_priority(numbers, group)
print(numbers)

# WHy about code worked?
# THere are three reasons this function operators as expected:

# 1. python support closures--that is, functions that refer to variables from the scope in which they were defined.
# This is why the helper unction is able to access the group argument for sort_priority

# 2. Functions are first-class objects in python, which means you can refer them directly, assign them to variables,
# pass them as arguments to other functions, compare them in expressions and if statements, and so on.
# This is how the sort method can accept a closure function as the key argument

# 3. Python has specific rules for comparing sequences(including tuples). it first compare items at index zero;
# then if those are equal, it compares items at index one, if they are still equal, it compares items at index two.
# This is why the return value from the helper closure causes the sort order to have two distinct groups.




