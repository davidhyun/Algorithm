import sys

def dfs(start=1):
    visited.append(start)

    for node in nodes[start]:
        if node not in visited:
            dfs(node)

    return visited

def bfs(start=1):
    q = [] # 앞으로 방문할 노드
    q.append(start)
    visited = [0 for _ in range(computers+1)] # 방문한 노드

    while q:
        com = q.pop()
        visited[com] = 1

        for x in nodes[com]:
            if visited[x] == 0:
                q.append(x)

    return visited

computers = int(sys.stdin.readline())
links_num = int(sys.stdin.readline())

nodes = [[] for _ in range(computers+1)]
visited = [] # for dfs
for i in range(links_num):
    (node_x, node_y) = map(int, sys.stdin.readline().split())
    nodes[node_x].append(node_y)
    nodes[node_y].append(node_x)

print(nodes)

print(len(dfs(start=1))-1) # 1번 자기자신을 제외한 감염시킨 컴퓨터 수
print(bfs(start=1).count(1)-1) # 1번 자기자신을 제외한 감염시킨 컴퓨터 수
