queue = [None for _ in range(3)]
front = rear = -1

# Enqueue
rear += 1; queue[rear] = "A"
rear += 1; queue[rear] = "B"
rear += 1; queue[rear] = "C"
print(queue) # ['A', 'B', 'C']

# Dequeue
front += 1; print(queue[front]); queue[front] = None # A
print(queue, "front =", front, "rear =", rear) # [None, 'B', 'C'] front = 0 rear = 2

front += 1; print(queue[front]); queue[front] = None # B
print(queue, "front =", front, "rear =", rear) # [None, None, 'C'] front = 1 rear = 2

front += 1; print(queue[front]); queue[front] = None # C
print(queue, "front =", front, "rear =", rear) # [None, None, None] front = 2 rear = 2

rear += 1; queue[rear] = "D" # Error
