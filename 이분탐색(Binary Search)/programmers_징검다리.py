# distance의 최대값이 1,000,000,000이기 때문에 이분탐색을 시도해본다
import math


def solution(distance, rocks, n):
    rocks.sort() # O(n)
    rocks.append(distance)
    left, right = 0, distance

    answer = 0
    while left <= right:
        prev = 0 # 이전 바위
        distance_min = math.inf # 각 mid에서 최소값이 저장되는 변수
        removed_rocks = 0 # 제거한 바위의 개수

        mid = (left + right) // 2 # 바위간 거리의 최소값을 mid로 잡겠다(거리가 mid 이하이면 모두 삭제)

        # 거리 재기
        for i in range(len(rocks)):
            # 두 바위의 거리가 mid 보다 작으면 바위 제거
            if rocks[i] - prev < mid:
                removed_rocks += 1

            # 두 바위의 거리가 mid 보다 길거나 같으면 바위는 그대로 두고 이전바위를 현재바위로
            else:
                distance_min = min(distance_min, rocks[i] - prev)
                prev = rocks[i]

        # 삭제한 바위가 n보다 많으면 mid를 줄여서 바위를 조금만 제거하기
        if removed_rocks > n:
            right = mid - 1

        # 삭제한 바위가 n보다 적거나 같으면 mid를 늘려서 바위를 더 제거하기
        else:
            answer = distance_min
            left = mid + 1

    return answer


distance = 25
n = 2
rocks = [2, 14, 11, 21, 17]
print(solution(distance, rocks, n))


"""
# 시간초과
# itertools의 permutations와 combinations은 시간복잡도가 크기 때문에 사용을 지양하는 편이다
from itertools import combinations


def solution(distance, rocks, n):
    check_point = [0] + rocks + [distance]
    rocks_to_be_removed = combinations(rocks, n) # 5C2 (중복허용X)

    answer = []
    for removed_rocks in rocks_to_be_removed:

        removed_point = list(set(check_point) - set(removed_rocks))

        inter_rock = []
        for i in range(1, len(removed_point)):
            gap = removed_point[i] - removed_point[i-1]
            inter_rock.append(gap)

        answer.append(min(inter_rock))

    return max(answer)
"""
