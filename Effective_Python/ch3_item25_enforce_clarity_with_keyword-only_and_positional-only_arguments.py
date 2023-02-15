# Passing arguments by keyword is powerful feature of python functions.

# The flexibility of keyword arguments enables you to write functions for many use cases.

# too many arguments may cause position-confusing, and this is exception-ignoring behavior, cause bugs
# that are hard to track down.

# One way to improve the readability of this code is to use keyword arguments.

# But the problem is here: keyword arguments are optional behavior, there's nothing forcing callers to use
# keyword arguments for clarity.

# defining keyword-only arguments, the arguments can only be supplied by keyword, never by position.

# use the * symbol in the argument list to indicated the end of positional arguments and the beginning of keyword-only
# arguments.

# The / symbol in the argument list indicates where positional-only arguments end:
# the parameter between the / and * symbols in the argument may be passed either by position or by keyword.

def safe_division_e(numerator, denominator, /,
                    ndigits=10, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        fraction = numerator / denominator
        return round(fraction, ndigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else: raise

result = safe_division_e(1.0, 10**500, ndigits=3, ignore_overflow=True, ignore_zero_division=False)
print(result)
result = safe_division_e(22, 7)
print(result)
result = safe_division_e(22, 7, 5)
print(result)
result = safe_division_e(22, 7, ndigits=2)
print(result)

# Things to remember:
# 1. Keyword-only arguments force callers to supply certain arguments by keyword (instead of by position),
# which makes the intention of a function call clearer. Keyword-only arguments are defined after a single * in the argument list.

# 2. Positional-only arguments ensure that callers can’t supply certain parameters using keywords,
# which helps reduce coupling. Positional-only arguments are defined before a single / in the argument list.

# 3. Parameters between the / and * characters in the argument list may be supplied by position or keyword,
# which is the default for Python parameters.