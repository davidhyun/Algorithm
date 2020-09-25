#시간제한 2초를 준수하려면 for문 안에서 계산처리하지 말고 미리 함수를 정의한다
N = int(input())

def sum_digit(n):
    return sum(map(int, str(n)))

flag = False
for i in range(max(N-9*len(str(N)),0), N):
    if N == i + sum_digit(i):
        print(i)
        flag = True
        break

if flag == False:
    print(0)
