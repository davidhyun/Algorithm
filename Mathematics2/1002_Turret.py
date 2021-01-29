import sys

T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    r = ((x2-x1)**2 + (y2-y1)**2)**0.5 # 고정된 두 점 사이의 거리 (두 원의 중점사이의 거리)
    R = [r1, r2, r]
    M = max(R); R.remove(M)

    # 두 원이 일치하는 경우
    if r == 0 and r1 == r2:
        print(-1)

    # 두 원이 한 점에서 만나는 경우 (외접, 내접)
    elif r == r1 + r2 or r2 == r + r1 or r1 == r + r2:
        print(1)

    # 두 원이 만나지 않는 경우 (r,r1,r2 중 가장 긴 값이 나머지 두값의 합보다 큰 경우)
    elif M > sum(R):
        print(0)

    # 두 원이 두 점에서 만나는 경우
    else:
        print(2)