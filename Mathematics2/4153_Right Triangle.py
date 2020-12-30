import sys

while True:
    lines = list(map(int, sys.stdin.readline().split()))
    lines = sorted(lines)

    if sum(lines) == 0:
        break
    else:
        if lines[0]**2 + lines[1]**2 == lines[2]**2:
            print('right')
        else:
            print('wrong')