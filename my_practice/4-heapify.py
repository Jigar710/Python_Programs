import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)

heapq.heapify(heap)
print(heap)

heapq.heappop(heap)       #delete first element and print it
print(heap)

heapq.heappop(heap)
print(heap)

heapq.heappop(heap)
print(heap)

#everytime first element is smallest element