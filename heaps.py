======================================
Heaps(Mutable)
======================================
you need to import the following to use heaps in python
from heapq import heappush, heappop

by default heap is a min heap in python
---------------------------------------
heap = []

heappush(heap, x)
heappop(heap)
---------------------------------------
You need to use min Heap to find k largest elements and max heap for 
k smallest elements

for example
a = [1,2,3,4,5]
minHeap = []

for num in a:
    heappush(minHeap, num)
    if len(minHeap) > 2:
        heappop(minHeap)
        
print(minHeap) -> [4,5]

