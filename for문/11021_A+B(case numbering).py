import sys

T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #",i+1,": ",A+B, sep="")

"""
import sys

n = int(input())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print('Case #%d: %d'%(i+1, a + b))
"""