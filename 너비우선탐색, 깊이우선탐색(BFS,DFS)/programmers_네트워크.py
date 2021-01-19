from collections import deque


def dfs(start_computer, computers, visited):
    q = deque()
    q.append(start_computer)

    while q:
        com_num = q.popleft()
        # 자기 자신은 이미 방문한 것으로 처리
        if visited[com_num] == False:
            visited[com_num] = True

        for i in range(len(computers)):
            if computers[com_num][i] == 1 and visited[i] == False:
                q.append(i)


def solution(n, computers):
    networks = 0
    visited = [False for _ in range(n)]

    for i in range(n):
        if visited[i] == False:
            dfs(i, computers, visited)
            networks += 1

    return networks


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))