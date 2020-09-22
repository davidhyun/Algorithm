import sys

T = int(sys.stdin.readline())

for _ in range(T):
    times, string = sys.stdin.readline().split()

    P = ""
    for x in string:
        P = P + (x * int(times))
    print(P)