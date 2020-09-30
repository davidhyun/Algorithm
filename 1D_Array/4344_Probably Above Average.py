import sys

T = int(sys.stdin.readline())

l = []
for i in range(T):
    l.append(list(map(int, sys.stdin.readline().split())))
    N = l[i][0]

    sum = 0
    for j in range(1, len(l[i])):
        sum += l[i][j]

    l_overmean = []
    for k in range(1, len(l[i])):
        if l[i][k] > sum/N:
            l_overmean.append(l[i][k])
    ratio = (len(l_overmean)/(len(l[i])-1)) * 100
    print("%.3f%%" % ratio)
