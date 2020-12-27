import sys

# 소수: 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수
N = int(sys.stdin.readline())
num_list = sys.stdin.readline().split()
num_list = list(map(int, num_list))

result = 0 # 소수의 개수
for num in num_list:
    check = 0 # 숫자가 소수인지 체크하는 변수

    natural_number_list = [x+1 for x in range(num)]
    for natural_number in natural_number_list:
        if num % natural_number == 0:
            check += 1

    # 숫자가 1과 자기자신으로만 나누어지는 수이면 소수로 카운팅
    if check == 2:
        result += 1

print(result)