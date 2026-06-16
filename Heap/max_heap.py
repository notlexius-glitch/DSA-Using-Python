import heapq

arr = [5, 2, 8, 1]

arr = [-i for i in arr]

heapq.heapify(arr)

print(-arr[0])