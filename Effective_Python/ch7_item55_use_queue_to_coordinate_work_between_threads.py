# python use concurrency to coordinate their work.
# one concurrent work is : pipeline of functions

# pipeline work:
# pipeline work likes an assembly line used in manufacturing.

# pipeline have many phases in serial, with a specific function for each phase.

# works are constantly being added to the beginning of the pipeline.
# the functions can operate concurrently
# the work moves forward as each function complete until there are no phases remaining.

# the pipeline is good for work that includes blocking I/O or subprocesses.

# Example:
# build a system that will take a constant stream of images from digital camera,
# resize them, then add them to a photo gallery online.

# split above system into three phases of a pipeline:
# 1. download ---- trieve new images
# 2. resize ------ downloaded images are passed through the resize function
# 3. upload ------the resized images are consumed by the upload function.

# How to assemble a pipeline to to download/resize/upload work concurrently?

# first thing I need is a way to hand off work between the pipeline phases.

# can be modeled as a thread-safe producer-consumer queue
