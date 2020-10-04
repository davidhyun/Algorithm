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

"""
# flag 없이 함수정의로 스택 문제풀이

import sys

def valid_check(ps):
    check_list = []
    for x in ps:
        if x == "(":
            check_list.append(x)
        elif x == ")":
            if not check_list:
                return False
            else:
                check_list.pop()

    return True if not check_list else False

T = int(sys.stdin.readline())
for _ in range(T):
    ps = sys.stdin.readline().strip()
    print("YES" if valid_check(ps) else "NO")
"""