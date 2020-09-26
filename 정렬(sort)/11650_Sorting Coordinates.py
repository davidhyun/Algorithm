import sys

T = int(sys.stdin.readline())

l = []
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    l.append([x,y])

for c in sorted(l, key=lambda c: [c[0], c[1]]):
    print(*c)


