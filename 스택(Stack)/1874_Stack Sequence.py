import sys

n = int(sys.stdin.readline())

num = 1
stack = []
result = []
flag = True

for _ in range(n):
    sequence_num = int(sys.stdin.readline())

    while num <= sequence_num:
        stack.append(num)
        result.append("+")
        num += 1

    if stack[-1] == sequence_num:
        stack.pop()
        result.append("-")
    else:
        flag = False
        continue

if flag == False:
    print("NO")
else:
    print("\n".join(result))