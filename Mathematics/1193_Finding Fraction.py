N = int(input())

line = 1
while N > line:
    N -= line
    line += 1

if line % 2 == 0:
    i = N
    j = line - N + 1
else:
    i = line - N + 1
    j = N

print(str(i) + '/' + str(j))