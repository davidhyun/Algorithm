# 입력받는 n의 최대값에 대한 소수들을 에라토스테네스의 체 방법으로 미리 찾아놓는다
N = 123456 * 2 + 1      # 첫번째 인덱스는 버림
sosu = [True] * N       # 배열을 소수로 초기화
sosu[0] = False; sosu[1] = False

for i in range(2, int(N**0.5)+1):
    if sosu[i] == True:
        for k in range(2*i, N, i):
            sosu[k] = False


# 소수의 개수를 찾는 함수정의
def count_prime(n):
    cnt = 0
    for i in range(n+1, 2*n+1):
        if sosu[i] == True:
            cnt += 1
    print(cnt)

while True:
    n = int(input())
    if n == 0:
        break

    count_prime(n)