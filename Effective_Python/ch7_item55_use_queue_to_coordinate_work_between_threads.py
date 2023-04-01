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

"""
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
processed = len(done_queue.items)
polled = sum(t.polled_count for t in threads)
print(f'Processed {processed} item after polling {polled} items')
"""



# The problems above:
# 1. the worker functions vary in their respective speeds, determining that all of the input work is complete
# requires yet another busy wait on the done_queue.

# 2. Second, in worker, the run method will execute forever in its busy loop.
# there is no obvious way to signal to a worker thread that it's time to exit

# 3. a backup in the pipeline can cause the program to crash arbitrarily.

# if the first phase makes rapid progress but the second phase makes slow progress, then the queue conncting
# the first phase to the second phase will constantly increase in size.
# the second phase won't be able to keep up.
# Given enough time and input data, the program will eventually run out ot memory and die.

# The above lesson isn't that pipelines are bed,
# it's that it's hard to build a good producer-consumer queue yourself.


# How to Solve the problems above?
# Solution: Queue to the rescue

# Queue class from the queue built-in module solve all the problems

# Why?
# 1. Queue eliminates the busy waiting in the worker by making the get method block until the new data is available

# Example:
# 1. Start a thread that waits for some input data on a queue:

from queue import Queue

my_queue = Queue()

def consumer():
    print("Consumer waiting")
    my_queue.get()
    print("Consumer done")
"""
thread = Thread(target=consumer)
thread.start()

# The above thread is running first
# the above thread won't finish until an item is put on the Queue instance and the get method has something to return.
print("Producer putting")
my_queue.put(object())
print("Producer done")
thread.join()
"""


# How to solve the pipeline backup issue?
# The queue class lets your specify the maximum amount of pending work to allow between two phases.
# the buffer size causes calls to put to block when the queue is already full.

# define a thread that waits for a while before consuming a queue.

my_queue = Queue()

def consumer():
    time.sleep(0.1)
    my_queue.get()
    print('Consumer got 1')
    my_queue.get()
    print('Consumer got 2')
    print('Consumer Done')
"""
thread = Thread(target=consumer)
thread.start()

my_queue.put(object())
print("Producer put 1")
my_queue.put(object())
print("Producer put 2")
print("Producer done")
thread.join()
"""



# The wait allow the producer thread to put both objects on the queue before the consumer thread ever calls get.
# the queue size is one, this means the producer adding items to the queue will have to wait for the consumer thread to call
# get at least one before the second call to put will stop blocking and add the second item to the queue.



# The queue class use task_done method to track the progress of work.
# track_done:
# lets you wait for a phase's input queue to drain and eliminates the need to poll the last phase of a pipeline.

in_queue = Queue()

def consumer():
    print("Consumer waiting")
    work = in_queue.get()
    print("Consumer working")
    # doing sth
    ...
    print("Consumer done")
    in_queue.task_done()

thread = Thread(target=consumer)
thread.start()

# the producer code doesn't have to join the consumer thread or poll.
# the producer wait for the in_queue to finish by calling join on the Queue instance.
# Even once it's empty, the in_queue won't be joinable until after task_done is called for every item that was
# ever enqueued:
print("Producer putting")
in_queue.put(object())
print("Producer waiting")
in_queue.join()
print("Producer done")
thread.join()

# define a Queue subclass to put all behavior together to
# tell the worker thread when it should stop processing

class ClosableQueue(Queue):
    SENTINEL = object()

    # define a close method that adds a special sentinel item to the queue
    # the sentinel item indicates there will be no more input items after it.
    def close(self):
        self.put(self.SENTINEL)


    # define an iterator for the queue thtat looks for this special object
    # and stop iteration when its found.
    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


download_queue = ClosableQueue()
resize_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()
threads = [
    StoppableWorker(download, download_queue, resize_queue),
    StoppableWorker(resize, resize_queue, upload_queue),
    StoppableWorker(upload, upload_queue, done_queue),
]


for thread in threads:
    thread.start()

for _ in range(1000):
    download_queue.put(object())
download_queue.close()

download_queue.join()
resize_queue.close()
resize_queue.join()
upload_queue.close()
upload_queue.join()
print(done_queue.qsize(), 'items finished')
for thread in threads:
    thread.join()



# extended to use multiple worker threads per phase to
# increase I/O parallelism and speed up this type of program significantly

def start_threads(count, *args):
    threads = [StoppableWorker(*args) for _ in range(count)]
    for thread in threads:
        thread.start()
    return threads

def stop_threads(closable_queue, threads):
    for _ in threads:
        closable_queue.close()

    closable_queue.join()
    for thread in threads:
        thread.join()

download_queue = ClosableQueue()
resize_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()

download_threads = start_threads(3, download, download_queue, resize_queue)
resize_threads = start_threads(6, resize, resize_queue, upload_queue)
upload_threads = start_threads(7, upload, upload_queue, done_queue)

for _ in range(1000):
    download_queue.put(object())

stop_threads(download_queue, download_threads)
stop_threads(resize_queue, resize_threads)
stop_threads(upload_queue, upload_threads)
print(done_queue.qsize(), 'items finished')
