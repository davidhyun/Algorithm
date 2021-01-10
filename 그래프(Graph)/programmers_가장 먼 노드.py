from collections import deque


def solution(n, vertex):
    adjacent_nodes = [[] for _ in range(n+1)] # 인접 노드 리스트(첫번째 인덱스는 1부터 사용)
    for i, j in vertex:
        adjacent_nodes[i].append(j)
        adjacent_nodes[j].append(i)

    distance = [0] * (n+1)
    is_visited = [False] * (n+1)


    q = deque()
    q.append(1) # start_node = 1
    is_visited[1] = True

    while q:
        current_node = q.popleft()

        for linked_node in adjacent_nodes[current_node]:
            if is_visited[linked_node] == False:
                is_visited[linked_node] = True
                distance[linked_node] = distance[current_node] + 1
                q.append(linked_node)

    return distance.count(max(distance))

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n=6, vertex=vertex))