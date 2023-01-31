# The problem: what happened if the return value is zero?
# if the return value is zero, it can cause issue when you evaluate the result in a condition like an if statement.
# You might accidentally look for any False equivalent value to indicate error instead of only looking for none.
# The misinterpretation of a False-equivalent return value is common mistake in Python code when None has special meaning

# How to solve the misinterpretation of a False-equivalent return value?
# The first way: split the return value into a two-tuple, the first part of the tuple
# indicates that the operation was a success or failure, the second part is the actual result that was computed.

# the return two-tuple  problem: callers of this function have to unpack the tuple, callers can easily ignore the first
# part of the tuple.

# the second better way to reduce these errors is to never return None for special cases.
# Instead, raise an exception up to the caller and have the caller deal with it.

# Input, Output, and exceptional behavior is clear, and the chance of a caller doing the wrong thing is extremely low.
def careful_divide(a: float, b: float) -> float:
    """
    Raises:
        ValueError: When the inputs cannot be devided
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')


# Things to remember:
# Functions that return None to indicate special meaning are error prone because None and other values
# Error Prone: zero and empty string all evaluate to False in conditional expressions

# Raise exceptions to indicate special situations instead of returning None.

# Type annotations can be used to make it clear that a function will never return the value None, even in special situations



