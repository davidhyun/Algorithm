import sys

A = sys.stdin.readline()
B = sys.stdin.readline()
C = sys.stdin.readline()

result = str(int(A) * int(B) * int(C))

count = [0,0,0,0,0,0,0,0,0,0,0]

#17037300
for i in result:
    count[int(i)] += 1

#print(count)

for i in range(10):
    print(count[i])
