num = int(input())
hansu_cnt = 0

for n in range(1, num+1):
    if n <= 99: # 1~99는 모두 한수
        hansu_cnt += 1
    else:
        nums = list(map(int, str(n)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            hansu_cnt += 1
print(hansu_cnt)