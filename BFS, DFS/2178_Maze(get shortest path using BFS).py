import sys
from collections import deque

# BFS는 각 정점을 최단경로로 방문
def bfs(x,y):
    q = deque()
    q.append((x,y,1))
    visited = [[0] * M for _ in range(N)] # 이미 지나온 길은 1로
    visited[x][y] = 1

    while q:
        x, y, cell_num = q.pop()
        if x == (N - 1) and y == (M - 1):
            return cell_num

        global direction
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < N and 0 <= ny < M:
                if maze_map[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.appendleft((nx,ny,cell_num+1))
                    visited[nx][ny] = 1

N, M = map(int, sys.stdin.readline().split())
maze_map = []
for _ in range(N):
    maze_map.append(list(map(int, list(sys.stdin.readline().strip()))))
direction = [[-1,0], [1,0], [0,-1], [0,1]] # 상하좌우

print(bfs(0,0))