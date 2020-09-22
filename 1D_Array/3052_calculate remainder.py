import sys

num = [int(sys.stdin.readline()) for i in range(10)]
#print(num)

num_div = []
for x in num:
    num_div.append(x%42)
#print(num_div)

Deduplication = set(num_div) # set()으로 중복제거
print(len(Deduplication))