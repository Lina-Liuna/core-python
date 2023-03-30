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


from collections import deque
from threading import Lock

class MyQueue:
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    # my digital camera is the producer, add new images to the end of the deque of pending items
    def put(self, item):
        with self.lock:
            self.items.append(item)

    # first phase of the processing pipeline is the consumer, removes images from the front of the deque of pending items
    def get(self):
        with self.lock:
            return self.items.popleft()


# Represent each phase of the pipeline as a Python thread:
# 1. takes work from one queue
# 2. runs a function on it
# 3. put the results on another queue.

# 3. track how many times the worker has checked for new input
# 4. track how much work it's completed

from threading import Thread
import time

class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_down = 0

    # trickiest part: the worker thread must properly handle the case where the input queue is empty
    # the input queue is empty means the previous phase hasn't completed its work yet.
    # can think this as a holdup in the assembly line
    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                # queue empty, no work to do
                time.sleep(0.01)
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_down += 1

def download(item):
    pass
def resize(item):
    pass
def upload(item):
    pass
# connect the three phases together by creating the queues
# for their coordination points and the corresponding worker threads:
download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()
threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue)
]

# starts threads
for thread in threads:
    thread.start()

# inject a bunch of work into the first phase of the pipeline:
for _ in range(1000):
    # use a plain object instance as a proxy for the real data required by the download function
    print('inject work into download queue')
    download_queue.put(object())

# wait for all of the items to be processed by the pipeline and end up in the done_queue:
while len(done_queue.items) < 1000:
    # do somthing
    print('wait all the items to be processed')
    ...

print('all the processes are done')

