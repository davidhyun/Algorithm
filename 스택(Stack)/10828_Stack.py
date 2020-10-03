import sys

N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    order = sys.stdin.readline().split()

    # push X : 정수 X를 스택에 넣는 연산
    if order[0] == "push":
        stack.append(int(order[1]))

    # top : 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우 -1 출력
    elif order[0] == "top":
        cnt_int = 0
        for i in range(len(stack)):
            if type(stack[i]) == type(1):
                cnt_int += 1
        if cnt_int > 0:
            print(stack[-1])
        elif cnt_int == 0:
            print(-1)

    # size : 스택에 들어있는 정수의 개수를 출력한다
    elif order[0] == "size":
        cnt_int = 0
        for i in range(len(stack)):
            if type(stack[i]) == type(1):
                cnt_int += 1
        print(cnt_int)

    # empty : 스택이 비어있으면 1, 아니면 0 출력
    elif order[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    # pop : 스택에서 가장 위에 있는 정수를 빼내서, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1 출력
    elif order[0] == "pop":
        if stack:
            print(int(stack.pop()))
        else:
            print(-1)