import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i]: i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end=" ")

# list.index(i)는 시간복잡도 O(N)
# dictionary[i]는 시간복잡도 O(1)