import math

a, b, c = map(int, input().split())

if c - b > 0:
    if a % (c-b) == 0:
        print(math.ceil(a/(c-b)) + 1)
    else:
        print(math.ceil(a/(c-b)))
else:
    print(-1)