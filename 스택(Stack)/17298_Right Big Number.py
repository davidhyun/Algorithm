N = int(input())
nums = list(map(int, input().split())) # 3 5 2 7

result = [-1] * N
stack = []

for i in range(N):
    # stack이 비어있지 않으면서 다음수가 해당수 보다 크면
    while len(stack) != 0 and nums[stack[-1]] < nums[i]:
        result[stack.pop()] = nums[i]

    stack.append(i)

print(*result)