from collections import deque

# BFS 너비우선탐색 (Queue 활용)
def bfs(numbers, target):
    q = deque() # 앞으로 처리할 작업공간

    initial_position = (0,0)
    q.append(initial_position)

    answer = 0
    while q:
        current_position, idx = q.popleft()

        # numbers의 길이만큼 모두 탐색했는데 현재 위치가 3이면 answer += 1
        if idx == len(numbers):
            if current_position == target:
                answer += 1

        else:
            number = numbers[idx]

            # 2 directions
            global direction
            for d in direction:
                if d == '+':
                    next_position = current_position + number
                    q.append((next_position, idx+1))
                elif d == '-':
                    next_position = current_position - number
                    q.append((next_position, idx+1))

    return answer


direction = ['+', '-']
numbers = [1,1,1,1,1]
target = 3
print(bfs(numbers, target))


"""
# DFS 깊이우선탐색 방법 (재귀함수 호출)
# 이 문제의 경우 DFS 깊이우선탐색 풀이가 BFS 너비우선탐색보다 각 케이스마다 수행시간이 2배 더 걸린다.
def dfs(idx, numbers, target, current_position):
    global answer

    if idx == len(numbers):
        if current_position == target:
            answer += 1
            return answer

    else:
        dfs(idx+1, numbers, target, current_position + numbers[idx])
        dfs(idx+1, numbers, target, current_position - numbers[idx])


def solution(numbers, target):
    dfs(0, numbers, target, 0)
    return answer

answer = 0
numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))
"""


