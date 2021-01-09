# 처음 짰던 코드: 시간복잡도는 O(n) 스케일이지만 간결하지않다.
def solution(n, lost, reserve):
    cloth_cnt = [1] * n

    for i in range(len(lost)):
        cloth_cnt[lost[i]-1] -= 1

    for j in range(len(reserve)):
        cloth_cnt[reserve[j]-1] += 1

    for i in range(len(cloth_cnt)):
        try:
            if cloth_cnt[i] == 0:
                if i >= 1: # i=0일 때 i-1이 -1로 배열 마지막부분을 가리키게되는 것을 방지
                    if cloth_cnt[i-1] == 2:
                        cloth_cnt[i-1] -= 1
                        cloth_cnt[i] += 1
                    elif cloth_cnt[i+1] == 2:
                        cloth_cnt[i+1] -= 1
                        cloth_cnt[i] += 1

                elif i == 0:
                    if cloth_cnt[i+1] == 2:
                        cloth_cnt[i+1] -= 1
                        cloth_cnt[i] += 1
            else:
                continue

        except:
            continue

    answer = 0
    for cnt in cloth_cnt:
        if cnt >= 1:
            answer += 1

    return answer

# 간결한 함수작성이지만 반복문안에 in과 remove 사용으로 시간복잡도는 O(n^2) 스케일이다.
def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for r in _reserve:
        before = r - 1
        after = r + 1
        if before in _lost:
            _lost.remove(before)
        elif after in _lost:
            _lost.remove(after)

    return n - len(_lost)

# 전체적인 시간복잡도는 O(n^2)이지만 solution2보다는 짧다.
def solution3(n, lost, reserve):
    _reserve = list(set(reserve) - set(lost)) # set() 함수는 리스트와 달리 교집합, 합집합 연산이 가능하다.
    _lost = list(set(lost) - set(reserve)) # set()의 시간복잡도: O(1)

    for r in _reserve:
        before = r - 1
        after = r + 1
        if before in _lost:
            _lost.remove(before)
        elif after in _lost:
            _lost.remove(after)

    return n - len(_lost)


# Case1
# n = 5
# lost = [2,4]
# reserve = [1,3,5]

# Case2
# n = 5
# lost = [2,4]
# reserve = [3]

# Case3
# n = 3
# lost = [1,2]
# reserve = [2,3]

# Case4
n = 5
lost = [1,2,4,5] # 여분 옷을 가졌던 학생도 도난당할 수 있음
reserve = [2,3,4]

print(solution(n, lost, reserve))
print(solution2(n, lost, reserve))
print(solution3(n, lost, reserve))