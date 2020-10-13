from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
index_list = list(map(int, sys.stdin.readline().split()))

dq = deque([x for x in range(1, N+1)])
total = 0
for i in index_list:
    cnt2 = cnt3 = 0
    if dq.index(i) == 0:
        dq.popleft()
    elif dq.index(i) != 0:
        if len(dq) - dq.index(i) >= dq.index(i):
            cnt2 = dq.index(i)
            total += dq.index(i)
            dq.rotate(-cnt2)
            dq.popleft()
        else:
            cnt3 = len(dq) - dq.index(i)
            total += cnt3
            dq.rotate(cnt3)
            dq.popleft()

print(total)
