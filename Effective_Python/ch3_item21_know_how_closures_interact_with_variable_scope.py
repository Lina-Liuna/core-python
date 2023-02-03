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


