import sys

N, K = map(int, sys.stdin.readline().split())
circular_queue = [x for x in range(1, N+1)]

front = 0
result = []
while circular_queue:
    front += (K-1)
    front = front % len(circular_queue)
    result.append(circular_queue.pop(front))
result = list(map(str, result))
print("<" + ", ".join(result) + ">")