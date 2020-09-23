import sys

T = int(sys.stdin.readline())

for _ in range(T):
    times, string = sys.stdin.readline().split()

    P = ""
    for x in string:
        P = P + (x * int(times))
    print(P)

"""
map은 seq의 요소하나하나 돌면서 function을 수행해서 맵 객체로 리턴
map(function, seq)
l = [(1,2),(2,3),(3,5),(2,9),(1,2)]
list(map(lambda x: x[0]+x[1], l)) # result = [3,5,8,11,3]

T = int(input())
for _ in range(T):
    N, word = input().split()
    print(*map(lambda x: x * int(N), word), sep = "")
"""
