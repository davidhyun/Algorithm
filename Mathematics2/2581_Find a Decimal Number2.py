M = int(input())
N = int(input())

result = []
for num in range(M,N+1):
    if num == 2:
        result.append(num)
    else:
        for natural_num in range(2,num+1):
            if num % natural_num == 0:
                break # 시간 단축
            elif natural_num == num-1:
                result.append(num)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)

"""
# 시간초과
import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

result = [] # 소수를 담는 리스트
num_list = [x for x in range(M, N+1)]
for num in num_list:
    check = 0 # 숫자가 소수인지 체크하는 변수

    for natural_num in [x+2 for x in range(num-1)]:
        if num % natural_num == 0:
            check += 1

    # 숫자가 1과 자기자신으로만 나누어지는 수이면 소수로 카운팅
    if check == 1:
        result.append(num)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)
"""