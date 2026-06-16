from collections import deque

queue = deque([1,2,3])

while queue:
    print(queue.popleft(), end=" ")