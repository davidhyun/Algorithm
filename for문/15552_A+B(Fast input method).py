import sys


T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)

"""
# 한 줄 입력받을 때
num = int(sys.stdin.readline()); print(num)

# 여러줄 입력받을 때
t = int(input())
num = [sys.stdin.readline() for i in range(t)]; print(num)
"""

