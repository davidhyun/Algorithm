# 함수 안에서 함수를 자기자신을 다시 호출하는 방식을 재귀호출이라 한다.
# 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1000으로 정해져있고 초과하면 RecursionError 발생함
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

N = int(input())
print(factorial(N))