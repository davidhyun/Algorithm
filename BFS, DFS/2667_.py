import sys
from collections import deque, Counter


def bfs(x,y, cnt):
    q = deque()
    q.append((x,y))

    direction = [[-1,0],[1,0],[0,-1],[0,1]] # 상하좌우
    while q:
        x, y = q.popleft()

        for d in direction:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx < size and 0 <= ny < size:
                if apartment_map[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = cnt
                    q.append((nx,ny))

    return None

size = int(sys.stdin.readline())

visited = [[0] * size for _ in range(size)]
apartment_map = []
for _ in range(size):
    apartment_map.append(list(map(int, list(sys.stdin.readline().rstrip()))))

cnt = 0
for i in range(size):
    for j in range(size):
        if apartment_map[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            bfs(i,j, cnt)

print(cnt)
print(visited)
ans = [element for array in visited for element in array]

# if 0 in list(Counter(ans):
    list(Counter(ans)
print(list(Counter(ans)))

# print(list(Counter(ans).values()))
