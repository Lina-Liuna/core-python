# if we already have global interpreter lock(GIL)
# we can forgo using mutual-exclusion locks(mutexes) in the code altogether, right?

# Not truly the case.
# The GIL will not protect you although only one Python thread runs at a time.
# A threads operations on data structures can be interrupted between any two bytecode instructions in
# python interpreter.

