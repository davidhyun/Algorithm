import sys

N = int(sys.stdin.readline())
check = N
new_num = 0
count = 0
while True:
    a = N//10
    b = N%10
    new_num = 10*b + (a+b)%10
    count += 1
    N = new_num
    if new_num == check:
        break
print(count)