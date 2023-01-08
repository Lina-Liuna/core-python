# Spaces:
# 1. Use spaces instead of tabs for indentation
# 2. four spaces
# 3. line max length = 79 chars
# 4. functions and classes should be separated by two blank lines
# 5. In a class, methods should be separated by one blank line.
# 6. dictionary: no whitespace between each key and colon.

# Naming:
# 1. Functions, variables, and attributes should be in lowercase_underscore format
# 2. protected instance attributes should be in _leading_underscore format
# 3. Private instance attributes should be in __ double_leading underscore format
# 4. Classes should be in CapitalizedWord format.
# 5. Module-Level constants should be in ALL_CAPS format
# 6. Instance methods in classes should use self
# 7. class methods should use cls, which refers to the class, as the name of the first parameter.

# Expressions and Statements:
# 1. Use inline negation (if a is not b)
# 2. don't check for empty containers or sequences by comparing the length to zero(if len(somelist) == 0)
# use if not somelist and assume that empty values will implicitly evaluate to False.
# 3. if somelist is True

# Imports
# 1. import statements at the top of a file
# 2. import the foo module from within the bar package, you should use from bar import foo, not just import foo
# 3. import orders:
    # 1. standard library modules
    # 2. third-party module
    # 3. you own modules
    # imports in alphabetical order
# Pylint tool: 