# (1) 1
# (6) 2 3 4 5 6 7
# (12) 8 9 10 11 12 13 14 15 16 17 18 19
# (18) 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37
# (24) 38 39 40 41 ...

N = int(input())

result = 0
for i , value in enumerate(range(0, 100, 6)):
    result += value
    if N < result:
        print(i+1)
        break