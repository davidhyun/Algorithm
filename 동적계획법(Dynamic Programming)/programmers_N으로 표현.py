def solution(N, number):
    dp = []

    # N을 사용할 수 있는 횟수를 1부터 8까지 늘려간다.
    for i in range(1, 9):
        case_set = set() # 임시 케이스 셋
        basic_num = int(str(N) * i) # 사칙연산 없이 이어붙인 수
        case_set.add(basic_num)

        # dp[3]은 이전의 dp[1]과 dp[2]의 사칙연산 조합으로 만들어진다.
        for j in range(0, i-1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    case_set.add(x + y)
                    case_set.add(x - y)
                    case_set.add(x * y)

                if y != 0:
                    case_set.add(x // y) # 제한사항: 사칙연산에서 나머지는 무시

        if number in case_set:
            return i

        dp.append(case_set)

    return -1

print(solution(5, 12))