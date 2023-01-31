# The problem: what happened if the return value is zero?
# if the return value is zero, it can cause issue when you evaluate the result in a condition like an if statement.
# You might accidentally look for any False equivalent value to indicate error instead of only looking for none.
# The misinterpretation of a False-equivalent return value is common mistake in Python code when None has special meaning

# How to solve the misinterpretation of a False-equivalent return value?
# The first way: split the return value into a two-tuple, the first part of the tuple
# indicates that the operation was a success or failure, the second part is the actual result that was computed.

