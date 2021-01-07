def solution(answers):
    A_patterns = [1, 2, 3, 4, 5]
    B_patterns = [2, 1, 2, 3, 2, 4, 2, 5]
    C_patterns = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score_board = {'1': 0, '2': 0, '3': 0}
    for idx, answer in enumerate(answers):
        if A_patterns[idx % len(A_patterns)] == answer:
            score_board['1'] += 1
        if B_patterns[idx % len(B_patterns)] == answer:
            score_board['2'] += 1
        if C_patterns[idx % len(C_patterns)] == answer:
            score_board['3'] += 1

    # 딕셔너리에서 값이 최대인 Key를 반환
    luckyguys = [key for key, value in score_board.items() if value == max(score_board.values())]
    return list(map(int, luckyguys))

# answers = [1,2,3,4,5]
answers = [1,3,2,4,2]
print(solution(answers))