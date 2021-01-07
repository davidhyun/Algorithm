import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    mix_cnt = 0
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1

        second = heapq.heappop(scoville)

        heapq.heappush(scoville, first + second * 2)
        mix_cnt += 1

    return mix_cnt

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K)) # 2