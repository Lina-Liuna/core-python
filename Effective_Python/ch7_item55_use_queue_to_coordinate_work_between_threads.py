# python use concurrency to coordinate their work.
# one concurrent work is : pipeline of functions

# pipeline work:
# pipeline work likes an assembly line used in manufacturing.

# pipeline have many phases in serial, with a specific function for each phase.

# works are constantly being added to the beginning of the pipeline.
# the functions can operate concurrently
# the work moves forward as each function complete until there are no phases remaining.

# the pipeline is good for work that includes blocking I/O or subprocesses.

