def solution(triangle):
    # 처음 층은 윗층이 없으므로 다음 층부터
    for layer in range(1, len(triangle)):
        for node_idx in range(len(triangle[layer])):
            # 맨 첫 노드이면 바로 윗단계 맨 첫노드(왼쪽)만 더한다.
            if node_idx == 0:
                triangle[layer][node_idx] += triangle[layer-1][0]

            # 맨 끝 노드이면 바로 윗단계 맨 끝노드(오른쪽)만 더한다.
            elif node_idx == len(triangle[layer])-1:
                triangle[layer][node_idx] += triangle[layer-1][-1]

            # 둘 다 아닌 중심노드들이면 바로 위의 좌우 노드들 중 큰 수를 더한다.
            else:
                max_value = max(triangle[layer-1][node_idx-1], triangle[layer-1][node_idx])
                triangle[layer][node_idx] += max_value

    return max(triangle[-1]) # 마지막 층까지 지나왔을 때 경로 길이 최대값


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))


def solution2(triangle):
    # 양 사이드의 값들도 중심 노드처럼 윗 단계에서 선택될 수 있게끔 양 사이드에 dummy value 0을 추가
    triangle = [[0] + value + [0] for value in triangle]

    for i in range(1, len(triangle)):
        for j in range(1, i+2):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i- 1][j])

    return max(triangle[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution2(triangle))