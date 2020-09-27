import sys

T = int(sys.stdin.readline())

l = []
for i in range(T):
    age, name = sys.stdin.readline().replace("\n", "").split()
    l.append([i, age, name])

print("\n".join("{1} {2}".format(*x) for x in sorted(l, key=lambda x: [int(x[1]), x[0]])))
