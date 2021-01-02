import sys

# 4 <= n <= 10000에 대한 소수들을 에라토스테네스의 체 방법으로 미리 찾아놓는다
def seive(n):
    prime_list = [False, False] + [True] * (n - 1)

    for i in range(2, int(n**0.5) + 1):
        if prime_list[i] == True:
            for j in range(i*2, n+1, i):
                prime_list[j] = False

    return prime_list


prime_list = seive(10000)

T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())

    # 가능한 골드바흐의 파티션이 여러가지일 경우 두 수의 차가 적은 소수를 구하기 위해 입력받은 n의 중간부터 비교해 나간다.
    a = n // 2
    b = a
    while a > 0:
        if prime_list[a] and prime_list[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1


"""
# 시간초과
import sys
import bisect
import itertools


# 4 <= n <= 10000에 대한 소수들을 에라토스테네스의 체 방법으로 미리 찾아놓는다
def seive(n):
    is_prime = [False, False] + [True] * (n - 1)

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i] == True:
            for j in range(i*2, n+1, i):
                is_prime[j] = False

    return [num for num in range(2, n+1) if is_prime[num]]


prime_num = seive(10000) # 1229개의 소수를 담은 배열


T = int(input())
for _ in range(T):
    num = int(sys.stdin.readline())


    nCr = list(itertools.combinations(prime_num[:bisect.bisect_right(prime_num, num)], 2))
    for x in prime_num[:bisect.bisect_right(prime_num, num)]:
        nCr.append((x,x))

    Goldbach_partitions = []
    for (x,y) in nCr:
        if x + y == num:
            Goldbach_partitions.append((x,y, abs(x-y)))

    Goldbach_partitions = sorted(Goldbach_partitions, key=lambda x: x[2])
    print(Goldbach_partitions[0][0], Goldbach_partitions[0][1])
"""