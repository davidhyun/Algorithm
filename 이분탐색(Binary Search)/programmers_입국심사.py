# 문제의 핵심은 최소, 최대 범위를 구한 후 이분 탐색으로 범위를 좁혀가며 답을 구하는 것
# 최대 범위는 최악의 경우로 심사관 중 가장 오래걸리는 심사관에게만 계속 검사받는 경우
# 최소, 최대 범위의 중간값인 mid 시간에서 n명을 심사할 수 있는지 아닌지를 파악하며 이분 탐색을 진행

def binary_search(n, times):
    left = min(times) # 심사관 1명, 대기자 1명일 경우 최소시간
    right = max(times) * n # 최대 범위(최악의 경우)
    answer = 0

    while left <= right:
        # 한 심사관에게 주어진 시간
        mid = (left + right) // 2
        people = 0

        for time in times:
            # 각 심사관마다, 주어진 시간 동안 몇 명의 사람을 심사할 수 있는지
            people = people + mid // time

            # 모든 사람을 심사할 수 있으면 반복문을 탈출
            if people >= n:
                break

        # 모든 사람을 심사할 수 있는 경우 한 심사관에게 주어진 시간을 줄여본다 (1분 단위)
        if people >= n:
            answer = mid
            right = mid - 1

        # 모든 사람을 심사할 수 없는 경우 한 심사관에게 주어진 시간을 늘려본다 (1분 단위)
        elif people < n:
            left = mid + 1

    return answer

n = 6
times = [7, 10]
print(binary_search(n, times))