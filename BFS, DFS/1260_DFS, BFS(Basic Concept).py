import sys
from collections import deque

def dfs(V):
    visited.append(V)

    for node in link_list[V]:
        if node not in visited:
            dfs(node)
    return visited

def bfs(V):
    q = deque()
    q.append(V)
    visited = [0 for _ in range(N+1)]
    visited[V] = 1
    result = []

    while q:
        num = q.pop()
        result.append(num)

        for x in link_list[num]:
            if visited[x] == 0:
                q.appendleft(x)
                visited[x] = 1
    return result


N, M, V = map(int, sys.stdin.readline().split())

visited = []
link_list = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    link_list[a].append(b)
    link_list[b].append(a)
[x.sort() for x in link_list]

print(*dfs(V))
print(*bfs(V))