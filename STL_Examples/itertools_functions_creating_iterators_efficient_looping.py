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
# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 0, 0, 0, 0, 0]

result = itertools.accumulate(data, operator.add)
print(list(result))
# [1, 3, 6, 10, 15, 21, 28, 36, 45, 45, 54, 62, 69, 75]

result = itertools.accumulate(data, max)
print(list(result))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9]

# Amortize a 5% loan of 1000 with 4 annual payments of 90
cashflows = [1000, -90, -90, -90, -90]
result = itertools.accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt)
print(list(result))
# [1000, 960.0, 918.0, 873.9000000000001, 827.5950000000001]


# itertools.repeat()
# Make an iterator that returns object over and over again.
# Runs indefinitely unless the times argument is specified
# A common use for repeat is to supply a stream of constant values to map or zip:
result = map(pow, range(10), itertools.repeat(2))
print(list(result))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

result = map(pow, range(10), itertools.repeat(3))
print(list(result))
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]


# itertools.islice(iterable, start, stop) Example
# Make an iterator that returns selected elements from the iterable.
# If start is non-zero, then elements from the iterable are skipped until start is reached.
a = 'abcedfg'
print(list(itertools.islice(a, 2, 4)))
print(list(itertools.islice(a, 2, 4)))
