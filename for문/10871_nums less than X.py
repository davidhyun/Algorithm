import sys

N, X = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
remain = []
for i in range(N):
    if A[i] < X:
        remain.append(A[i])
print(*remain) # unpacking
