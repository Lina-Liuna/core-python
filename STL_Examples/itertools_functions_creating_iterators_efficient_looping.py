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

# Amortize a 5% loan of 1000 with 4 annual payments of 90
cashflows = [1000, -90, -90, -90, -90]
result = itertools.accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt)
print(list(result))

# itertools.repeat()
# Make an iterator that returns object over and over again.
# Runs indefinitely unless the times argument is specified
# A common use for repeat is to supply a stream of constant values to map or zip:
result = map(pow, range(10), itertools.repeat(2))
print(list(result))

result = map(pow, range(10), itertools.repeat(3))
print(list(result))