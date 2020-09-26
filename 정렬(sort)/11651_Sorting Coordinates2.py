import sys

N = int(sys.stdin.readline())

l = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    l.append((a,b))

print("\n".join("{0} {1}".format(*n) for n in sorted(l, key=lambda x: (x[1], x[0]))))

"""
.split()의 반대가 .join()
join() 함수의 리턴은 STRING
"""
