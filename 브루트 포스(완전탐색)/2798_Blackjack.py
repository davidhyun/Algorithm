# Blackjack
import sys

N, M = map(int, sys.stdin.readline().split())
cards = []
cards.extend(map(int, sys.stdin.readline().split()))

# 모든 경우의 수
all_cases = []
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            all_cases.append([cards[i], cards[j], cards[k]])

#print(all_cases)
sum_cases = list(map(sum, all_cases))

# 3장을 뽑은 모든 경우의 수를 합한 것 중에 최대값 찾기
current_max = 0
for i in range(len(sum_cases)):
    if sum_cases[i] > current_max and sum_cases[i] <= M:
        current_max = sum_cases[i]
print(current_max)
