import heapq

# This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm

# Heaps are binary trees for which every parent node has a value less than or equal to any of its children. This
# implementation uses arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, counting elements
# from zero.

# The interesting property of a heap is that its smallest element is always the root, heap[0]

# A heapssort can be implemented by pushing all values onto a heap and then popping off the smallest values
# one at a time

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

l = [9,8,6,5,4,3,21]
sorted_l = heapsort(l)
print(sorted_l)

