from collections import Counter

# case1
# participant = ['leo', 'kiki', 'eden']
# completion = ['eden', 'kiki']

# case2
# participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
# completion = ['josipa', 'filipa', 'marina', 'nikola']

# case3
participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']


def solution(participant, completion):
    dic = Counter(participant) # 파이썬의 dictionary로 hash table 구조를 구현할 수 있다.
    for x in completion:
        if x in dic.keys():
            dic[x] -= 1

    for key, value in dic.items():
        if value != 0:
            return key

def solution2(participant, completion):
    participant.sort()
    completion.sort()

    # Counter 객체는 교집합(-)과 합집합(+) 연산이 가능하다
    answer = Counter(participant) - Counter(completion)

    return list(answer)[0]

print(solution(participant, completion))
print(solution2(participant, completion))