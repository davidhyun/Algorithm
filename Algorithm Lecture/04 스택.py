stack = [None for _ in range(5)]
top = -1 # top의 인덱스(마지막 인덱스)

# push
top += 1; stack[top] = "커피"
top += 1; stack[top] = "녹차"
top += 1; stack[top] = "꿀물"
print(stack) # ['커피', '녹차', '꿀물', None, None]

# pop
print("뽑기 -->", stack[top]) # 뽑기 --> 꿀물
stack[top] = None
top -= 1
print(stack) # ['커피', '녹차', None, None, None]