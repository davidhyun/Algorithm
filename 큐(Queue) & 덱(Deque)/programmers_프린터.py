from collections import deque


def solution(priorities, location):
    q = deque([(loc, priority) for (loc, priority) in enumerate(priorities)])
    result = []
    flag = False
    while q:
        inspection = q.popleft()
        for compare in q:
            if inspection[1] < compare[1]:
                flag = True

        if flag == True:
            q.append(inspection)
            flag = False
        else:
            result.append(inspection)
            for idx, x in enumerate(result, 1):
                if x[0] == location:
                    return idx

# CASE1
# priorities = [2,1,3,2]
# location = 2

# CASE2
priorities = [1,1,9,1,1,1]
location = 0

print(solution(priorities, location))