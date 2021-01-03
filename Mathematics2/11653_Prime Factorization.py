# 시간단축
num = int(input())
i = 2
r = int(num**0.5)

while i <= r:
    while num % i == 0:
        print(i)
        num = num // i

    i += 1

if num > 1:
    print(num)


"""
# 기본풀이
num = int(input())

while num != 1:
    for i in range(2, num+1):
        if num % i == 0:
            print(i)
            num = num // i
            break

# 시간초과
# 미리 입력받은 수의 소수들을 에라토스테네스의 체 방법으로 찾아놓는다
def sieve(n):
    is_prime = [False, False] + [True] * (n - 1)
    if n == 1:
        return None
    else:
        for i in range(2, int(n**0.5)+1):
            if is_prime[i] == True:
                for j in range(2*i, n+1, i):
                    is_prime[j] = False

        return [i for i in range(2, n+1) if is_prime[i]]

n = int(input())
prime_list = sieve(n)
while True:
    if prime_list == None:
        print()
        break

    for prime in prime_list:
        if n % prime != 0:
            continue
        elif n % prime == 0:
            print(prime)
            n = n // prime
            break

    if n in prime_list:
        print(n)
        break
"""