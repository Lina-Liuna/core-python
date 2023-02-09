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
