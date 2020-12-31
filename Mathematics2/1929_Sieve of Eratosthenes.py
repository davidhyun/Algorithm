# '에라토스테네스의 체': 소수를 찾는 방법 중 가장 효율적인 방법
# 어떤 수의 소수 여부를 확인할 때 그 숫자의 제곱근까지만 약수의 여부를 검증하면 O(N^1/2)의 시간 복잡도로 빠르게 구할 수 있다.
# 숫자 N을 수로 나누면 몫이 생기는데, 몫과 나누는 수 둘 중 하나는 N 제곱근 이하이기 때문이다.

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            # i는 특정 수
            if num % i == 0:
                return False
        return True

M, N = map(int, input().split())
for num in range(M, N+1):
    if isPrime(num):
        print(num)