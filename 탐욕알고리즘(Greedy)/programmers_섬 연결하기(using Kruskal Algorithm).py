# Kruskal 알고리즘 : 탐욕 알고리즘을 이용하여 네트워크의 정점을 최소비용으로 연결하는 알고리즘
# Kruskal 알고리즘의 핵심은 사이클이 생성되지 않게하는 것이다.
# 사이클이 생성되지 않기위한 조건으로는 추가하려는 간선의 양 끝점이 같은 집합에 속하지 않도록 하는 것이다. 이는 Union-Find 알고리즘으로 판별할 수 있다.


# Kruskal Algorithm
def solution(n, costs):
    min_cost = 0
    costs.sort(key=lambda x: x[2]) # 비용 기준으로 오름차순 정렬
    visited_node = set([costs[0][0]]) # 방문을 확인하는 셋에 cost가 작은 노드를 추가

    while len(visited_node) != n:
        for i, cost in enumerate(costs):
            # 이미 두 노드가 routes에 존재하면 continue
            if cost[0] in visited_node and cost[1] in visited_node:
                continue

            # 둘 중 하나만 routes에 존재하면 그 노드들을 셋에 추가
            elif cost[0] in visited_node or cost[1] in visited_node:
                visited_node.update([cost[0], cost[1]])
                min_cost += cost[2]
                costs[i] = [-1,-1,-1]
                break

    return min_cost


n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))