from collections import deque

queue = deque([1, 2])
# queue.append(3)
# queue.append(4)
# queue.append(5)
print(queue)
queue.popleft()
queue.popleft()
print(queue)

if not queue:
    print("Queue is empty")