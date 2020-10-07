# pop기능을 수행하면 가장 앞의 인덱스 cnt에 해당되는 부분을 출력하고 cnt에 1을 더해서 가장 앞쪽을 가르키는 인덱스를 그 다음칸을 가르키도록 한다
import sys

N = int(sys.stdin.readline())

l = []
cnt = 0 # 가장 앞쪽을 가르키는 인덱스
for _ in range(N):
    string = sys.stdin.readline()
    order = string.split()
    if order[0] == "push":
        l.append(order[1])

    elif order[0] == 'pop':
        if len(l) > cnt:
            print(l[cnt])
            cnt += 1
        else: print(-1)

    elif order[0] == 'size':
        print(len(l)-cnt)

    elif order[0] == 'empty':
        if len(l) == cnt :
            print(1)
            cnt = 0
            l = []
        else: print(0)

    elif order[0] == 'front':
        if len(l) > cnt: print(l[cnt])
        else: print(-1)

    elif order[0] == 'back':
        if len(l) > cnt: print(l[-1])
        else: print(-1)