import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    q = [x for x in range(1,N+1)] # 문서 리스트
    q[M] = 'target' # target 문서지정
    priority = list(map(int, sys.stdin.readline().split())) # 우선순위 리스트

    # print(q)
    # print(priority)
    result = []
    while q:
        # q의 첫번째 인덱스와 우선순위 최대값의 인덱스가 다르면 뒤로 밀림
        if q.index(q[0]) != priority.index(max(priority)):
            q.append(q.pop(0))
            priority.append(priority.pop(0))
        else:
            result.append(q.pop(0))
            priority.pop(0)

    # print(result)
    print(result.index('target')+1)
