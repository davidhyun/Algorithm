### 함수 선언부 ###
def isStackFull():
    if top == SIZE-1:
        return True
    else:
        return False

def isEmpty():
    if top == -1:
        return True
    else:
        return False

def push(data):
    global stack, top
    if isStackFull():
        print("스택 FULL")
        return
    top += 1
    stack[top] = data

def pop():
    global stack, top
    if isEmpty():
        print("스택이 비어있음")
        return
    #del stack[top] # 값도 공간도 삭제하고 정렬(시간소요)
    result = stack[top]
    stack[top] = None
    top -= 1
    return result


### 전역 변수부 ###
SIZE = 5 # 스택의 사이즈 제한
stack = [None for _ in range(SIZE)]
top = -1 # top의 인덱스(마지막 인덱스)


### 메인 코드부 ###
print(stack) # [None, None, None, None, None]
push(1); push(2); push(3); print(stack) # [1, 2, 3, None, None]
push(4); push(5); push(6); print(stack, "/ top =", top) # 스택 FULL, [1, 2, 3, 4, 5] / top = 4
pop(); pop(); pop(); pop(); pop(); pop(); print(stack, "/ top =", top) # 스택이 비어있음, [None, None, None, None, None] / top = -1
push("abc"); print(stack, "/ top =", top) # ['abc', None, None, None, None] / top = 0
