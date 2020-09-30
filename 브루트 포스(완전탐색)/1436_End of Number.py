import sys

N = int(sys.stdin.readline())

EoN = 666 # End of Number
while N:
    if "666" in str(EoN):
        N -= 1
    EoN += 1
print(EoN-1)

