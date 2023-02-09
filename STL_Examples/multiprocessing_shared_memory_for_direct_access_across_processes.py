# SharedMemory is multiprocessing's class
# SharedMemory used for allocation and management of shared memory to be accessed by one or more processes on a
# multicore or symmetric multiprocessor(SMP) machine.

# use multiprocessing.manager module to manage shared memory

# SharedMemory shared memory refers to "System V style" shared memory blocks, and doesn't refer to "distributed
# shared memory"

# SharedMemory permits distinct processes to potentially read and write to a common region of volatile memory.
# SharedMemory permits the sharing of data between processes, avoid the need to instead send messages between processes
# containing that data.

# Sharing data directly via memory can provide significant performance benefits compared to sharing data via disk.
import multiprocessing
from multiprocessing.shared_memory import SharedMemory

# low-level use of SharedMemory instances:

def low_level_use_of_SharedMemory():
    shm_a = SharedMemory(create=True, size=10)
    print(type(shm_a.buf))
    buffer = shm_a.buf
    print(len(buffer))
    buffer[:5] = bytearray([11,22,33,44,55])
    buffer[5] = 100
    shm_b = SharedMemory(shm_a.name)

    import array
    array.array('b', shm_b.buf[:5])

    print(shm_b)
    print(shm_b.buf)
    print(bytes(shm_b.buf))
    print(bytes(shm_b.buf[:10]))

    shm_b.buf[:5] = b'howdy'
    print(bytes(shm_b.buf[:10]))
    print(bytes(shm_a.buf[:10]))
    shm_b.close()
    shm_a.close()
    shm_a.unlink()
# low_level_use_of_SharedMemory()

import numpy as np

def shared_memory_with_numpy():
    a = np.array([1, 1, 2, 3, 5, 8])  # Start with an existing NumPy array
    shm = SharedMemory(create=True, size=a.nbytes)
    # Now create a NumPy array backed by shared memory
    b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
    b[:] = a[:]  # Copy the original data into shared memory
    print(b)
    print(type(b))
    print(type(a))
    print(shm.name)   # psm_ef7e100d

    existing_shm = SharedMemory(name=shm.name)
    c = np.ndarray((6,), dtype=np.int64, buffer=existing_shm.buf)
    print(c)

    del c
    existing_shm.close()
    del b
    shm.close()
    shm.unlink()

# shared_memory_with_numpy()

# basic mechanism of a SharedMemoryManager:
from multiprocessing.managers import SharedMemoryManager

def shared_memory_manager_func():
    smm = SharedMemoryManager()
    smm.start()  # Start the process that manages the shared memory blocks
    sl = smm.ShareableList(range(4))
    # print(sl)

# shared_memory_manager_func()   # Error happened



