# 함수는 호출할 때 Stack 방식을 사용한다
def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1

    return n * factorial(n-1)

print(factorial(5)) # 120