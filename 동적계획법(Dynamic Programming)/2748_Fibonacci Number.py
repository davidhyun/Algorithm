import sys


def fibonacci(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

N = int(sys.stdin.readline())
print(fibonacci(N))

"""
파이썬의 초기 재귀 깊이는 1000
import sys
sys.setrecursionlimit(100000) # 재귀깊이를 100000 으로 설정
"""