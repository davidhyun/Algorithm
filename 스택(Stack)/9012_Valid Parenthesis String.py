import sys

T = int(sys.stdin.readline())

for _ in range(T):
    PS = list(sys.stdin.readline().rstrip())

    check_cnt = 0
    for x in PS:
        if x == "(":
            check_cnt += 1
        elif x == ")":
            check_cnt -= 1

        # 여는 괄호 없이 닫는 괄호가 먼저나오면 뒤에는 볼 것도 없다
        if check_cnt < 0:
            print("NO")
            break

    if check_cnt == 0:
        print("YES")
    elif check_cnt > 0:
        print("NO")