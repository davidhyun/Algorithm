def d(n):
    result = n
    while n != 0:
        result += n%10
        n = n//10 # n //= 10
    return result

generated_nums = [] # 생성자
self_nums = [] # 셀프넘버

for i in range(1, 10001):
    generated_nums.append(d(i))
    if i not in generated_nums:
        self_nums.append(i)

for num in self_nums:
    print(num)
