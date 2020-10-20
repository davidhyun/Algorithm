import sys
from collections import deque

def bfs(riped):
    days = -1

    direction = [[-1,0], [1,0], [0,-1], [0,1]] # 상하좌우
    while riped:
        days += 1
        #cnt = 0
        for _ in range(len(riped)): # 처음에 두번돌기로 했으면 두번돈다
            #print(cnt)
            x, y = riped.popleft()

            for d in direction:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < N and 0 <= ny < M:
                    if tomato_map[nx][ny] == 0:
                        tomato_map[nx][ny] = 1
                        riped.append((nx,ny))
                        #print(riped)
            #cnt += 1

    for row in tomato_map:
        if 0 in row:
            return -1

    return days


M, N = map(int, sys.stdin.readline().split()) # 열, 행

tomato_map = []
riped = deque() # 익은 토마토의 위치가 저장되는 곳
for i in range(N): # 행
    tomato_map.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M): # 열
        if tomato_map[i][j] == 1:
            riped.append((i,j))

print(bfs(riped))
