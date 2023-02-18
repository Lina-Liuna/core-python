matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for row in matrix for x in row]
print(flat)

squared = [[x ** 2 for x in row] for row in matrix]
print(squared)

# Things to Remember
# 1. Comprehensions support multiple levels of loops and multiple con- ditions per loop level.
# 2. Comprehensions with more than two control subexpressions are very difficult to read and should be avoided.