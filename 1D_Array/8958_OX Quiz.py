import sys

T = int(sys.stdin.readline())

for i in range(T):
    ox = input()
    O_num = 0
    score = 0
    for j in range(len(ox)):
        if ox[j] == "O":
            O_num += 1
            score += O_num
        elif ox[j] == "X":
            O_num = 0
            score += 0
    print(score)

"""
input()과 sys.stdin.readline()의 차이

input은 입력받을 때 데이터자체만 받아오지만
sys.stdin.readline()는 데이터끝에 개행문자 '\n'까지 받아온다.
"""