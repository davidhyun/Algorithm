from collections import deque


def solution(progresses, speeds):
    pro_deq = deque(progresses)
    sp_deq = deque(speeds)

    answer = []
    day = 0
    cnt = 0

    while pro_deq:
        if (pro_deq[0] + day * sp_deq[0]) >= 100:
            pro_deq.popleft()
            sp_deq.popleft()
            cnt += 1
        else:
            if cnt != 0:
                answer.append(cnt)
                cnt = 0  # cnt 초기화
            day += 1

    answer.append(cnt)
    return answer

# CASE1
# progresses = [93,30,55]
# speeds = [1,30,5]

# CASE2
# progresses = [95,90,99,99,80,99]
# speeds = [1,1,1,1,1,1]

# print(solution(progresses, speeds))