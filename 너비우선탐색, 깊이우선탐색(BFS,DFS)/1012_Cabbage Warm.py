import sys
from collections import deque
sys.getrecursionlimit() # 1000
sys.setrecursionlimit(10000) # 실제 재귀깊이 2000 ~ 3000 사이

# DFS (재귀 호출)
def dfs(x,y):
    baechoo_map[x][y] = 0

    global direction
    for d in direction:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < Y and 0 <= ny < X:
            if baechoo_map[nx][ny] == 1:
                dfs(nx,ny)

# BFS (큐 이용)
def bfs(x,y):
    q = deque() # 앞으로 처리 예정
    q.appendleft((x,y))
    baechoo_map[x][y] = 0

    while q:
        x, y = q.pop()

        global direction
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < Y and 0 <= ny < X:
                if baechoo_map[nx][ny] == 1:
                    q.appendleft((nx, ny))
                    baechoo_map[nx][ny] = 0


T = int(sys.stdin.readline())
direction = [[-1,0], [1,0], [0,-1], [0,1]] # 상하좌우
for _ in range(T):
    X, Y, K = map(int, sys.stdin.readline().split()) # X, Y = 열, 행
    baechoo_map = [[0] * X for _ in range(Y)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        baechoo_map[y][x] = 1

    dfs_cnt = 0
    bfs_cnt = 0
    for x in range(Y):
        for y in range(X):
            if baechoo_map[x][y] == 1:
                dfs(x, y)
                dfs_cnt += 1
                bfs(x, y)
                bfs_cnt += 1

    print(dfs_cnt, bfs_cnt)



