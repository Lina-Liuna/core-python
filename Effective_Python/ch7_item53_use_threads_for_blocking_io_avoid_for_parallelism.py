# The standard implementation of python is called CPython
# CPython runs a python program in two steps;
# 1. parses and compiles the source text into bytecode(8-bit instructions)
# 2. CPython runs the bytecode using a stack-based interpreter.

# bytecode interpreter has state that must be maintained and coherent while the Python
# program executes.

# CPython enforces coherence with a mechanism called the global interpreter lock(GIL)


