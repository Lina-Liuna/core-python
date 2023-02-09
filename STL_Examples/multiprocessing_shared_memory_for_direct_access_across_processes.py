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
import multiprocessing as mp
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

low_level_use_of_SharedMemory()