from collections import defaultdict


def solution(n, results):
    answer = 0
    win = defaultdict(set) # 누구누구를 이긴다
    lose = defaultdict(set) # 누구누구한테 진다

    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)

    for boxer in range(1, n+1):
        # boxer에게 진 사람들은 boxer를 이긴 사람들에게 모두 진다.
        for loser in win[boxer]:
            lose[loser].update(lose[boxer])

        # boxer를 이긴 사람들은 모두 boxer가 이긴 사람들을 이긴다.
        for winner in lose[boxer]:
            win[winner].update(win[boxer])

    # 해당 선수의 지고, 이긴 선수의 개수 합이 n-1(자기자신 제외)이면 순위를 결정할 수 있다
    for boxer in range(1, n+1):
        if len(win[boxer]) + len(lose[boxer]) == n - 1:
            answer += 1

    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))