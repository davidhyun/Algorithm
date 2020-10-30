### collections 모듈의 deque 함수 ###
from collections import deque
import sys

def commands(p):
    if p[0] == "push_front":
        deq.appendleft(p[1])
    elif p[0] == "push_back":
        deq.append(p[1])
    elif p[0] == "pop_front":
        return print(deq.popleft()) if deq else print(-1)
    elif p[0] == "pop_back":
        return print(deq.pop()) if deq else print(-1)
    elif p[0] == "size":
        return print(len(deq))
    elif p[0] == "empty":
        return print(1) if not deq else print(0)
    elif p[0] == "front":
        return print(deq[0]) if deq else print(-1)
    elif p[0] == "back":
        return print(deq[-1]) if deq else print(-1)

deq = deque()
T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().strip().split()
    commands(p)