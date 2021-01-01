import sys
import bisect


# 입력받는 n의 최대값에 대한 소수들을 에라토스테네스의 체 방법으로 미리 찾아놓는다
def seive(n):
    is_prime = [False, False] + [True] * (n - 1)

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i] == True:
            for j in range(i*2, n+1, i):
                is_prime[j] = False

    return [num for num in range(2, n+1) if is_prime[num]]

prime_num = seive(123456 * 2) # 123456 * 2까지의 소수 숫자들을 담은 배열


for num in sys.stdin:
    num = int(num)
    if num == 0:
        break

    print(bisect.bisect(prime_num, num * 2) - bisect.bisect(prime_num, num))

"""
'bisect': 정렬된 순서로 List를 유지하고자 할 때 or 구간의 인덱스를 얻을 때도 유용하게 사용할 수 있다.
for문을 쓰지 않고도 각 구간별 검색을 빠르고 쉽게할 수 있다.

bisect.bisect_left(arr, x): arr가 정렬되어 있다는 가정하에 x값이 들어갈 위치를 반환 (경계값은 왼쪽으로 포함)
bisect.bisect_right(arr, x): arr가 정렬되어 있다는 가정하에 x값이 들어갈 위치를 반환 (경계값은 오른쪽으로 포함)
bisect.bisect = bisect.bisect_right

import bisect
arr = [100, 200, 300]

print(bisect.bisect_right(arr, 0)) # 숫자 0이들어갈 위치는 0
print(bisect.bisect_right(arr, 100)) # 숫자 100이들어갈 위치는 1
print(bisect.bisect_left(arr, 100)) # 숫자 100이들어갈 위치는 0
"""