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

"""
# 스택은 LIFO(Last In First Out)를 따른다. 즉, 가장 최근에 스택에 추가한 항목이 가장 먼저 제거될 항목이다
# 클래스를 활용한 스택 구현

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return not self.items
        
stk = Stack()           # stack 객체 생성
print(stk)              # stack object 생성 확인
print(stk.isEmpty())    # 처음에는 아무것도 들어있지 않으므로 True 출력
stk.push(1)             # stk에 1을 넣음
stk.push(2)             # stk에 2를 넣음
print(stk.pop())        # stk에서 2가 꺼내지면서 출력
print(stk.pop())        # stk에서 1이 꺼내지면서 출력
print(stk.isEmpty())    # 객체에 아무것도 들어있지 않으므로 True 출력
"""