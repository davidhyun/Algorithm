# '에라토스테네스의 체': 특정 범위가 주어지고 그 범위 내의 모든 소수를 찾을 때 가장 효율적인 방법
# 어떤 수의 소수 여부를 확인할 때 그 숫자의 제곱근까지만 약수의 여부를 검증하면 O(N^1/2)의 시간 복잡도로 빠르게 구할 수 있다.
# 숫자 N을 수로 나누면 몫이 생기는데, 몫과 나누는 수 둘 중 하나는 N 제곱근 이하이기 때문이다.

from itertools import permutations


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    prime_numbers = []
    for k in range(1, len(numbers)+1):
        # 1,2,3... numbers배열 길이만큼 써서 만들 수 있는 경우의 수 (중복허용)
        cases = list(map(''.join, permutations(list(numbers), k)))
        cases = list(set(map(int, cases)))

        for num in cases:
            if is_prime(num):
                prime_numbers.append(num)

    return len(set(prime_numbers))


print(solution('011'))