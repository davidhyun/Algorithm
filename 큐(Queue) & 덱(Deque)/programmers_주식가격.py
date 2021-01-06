from collections import deque


def solution(prices):
    deq = deque(prices)
    answer = []

    while True:
        if deq:
            interval_time = 0
            pre = deq.popleft()

            for value in deq:
                interval_time += 1
                if value < pre:
                    break

            answer.append(interval_time)

        else:
            break

    return answer

prices = [1,2,3,2,3]
print(solution(prices))