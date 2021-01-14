def solution(money):
    #####첫번째 집을 무조건 털고, 마지막 집은 털지 않는 경우 #####
    dp1 = [0] * len(money)
    dp1[0] = money[0] # 집이 하나만 있을 경우
    dp1[1] = max(money[0], money[1]) # 집이 두 집만 있을 경우

    for i in range(2, len(money)-1):
        # (1번째 전 집)과 (2번째 전 집 + 현재 집) 중 최대로 털 수 있는 집을 선택한다.
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

    ##### 마지막 집을 무조건 털고, 첫번째 집은 털지 않는 경우 #####
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)):
        # (1번째 전 집)과 (2번째 전 집 + 현재 집) 중 최대로 털 수 있는 집을 선택한다.
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

    return max(max(dp1), max(dp2))

money = [1,2,3,1]
print(solution(money))