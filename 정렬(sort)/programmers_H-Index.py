import bisect


def solution(citations):
    sorted_citations = sorted(citations)
    h = []

    # h는 배열의 길이보다 클 수 없다
    for i in range(len(sorted_citations)+1):
        if len(sorted_citations[bisect.bisect_left(sorted_citations, i):]) >= i:
            h.append(i)

    return max(h)


def solution2(citations):
    sorted_citations = sorted(citations)
    n = len(citations)

    for i in range(n):
        if sorted_citations[i] >= n-i:
            return n-i # H-Index가 큰 경우부터 찾기 때문에 빠르다

    return 0


citations = [5,5,5,5] # H-Index: 4
# citations = [0,0,0,0] # H-Index: 0
# citations = [3,0,6,1,5] # H-Index: 3
# citations = [10,8,5,4,3] # H-Index: 4
# citations = [25,8,5,3,3] # H-Index: 3
print(solution(citations))
print(solution2(citations))