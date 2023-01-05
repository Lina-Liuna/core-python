# itertools standardized a core set of fast, memory efficient tools
# tools are useful by themselves or in combination.
# tools work well with the high-speed functions in the operator module.

# itertools.accumulate
import itertools
import operator

# calc n!
data = [1,2,3,4,5,6,7,8,9,0,9,8,7,6]
result = itertools.accumulate(data, operator.mul)
print(list(result))

result = itertools.accumulate(data, operator.add)
print(list(result))

result = itertools.accumulate(data, max)
print(list(result))


