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

def safe_division_c(number, divisor, *,  # Changed
                    ignore_overflow=False,
ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise