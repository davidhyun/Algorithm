import sys

N = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().strip().split()))
new_score = [(l[i]/max(l) * 100) for i in range(N)]

print(sum(new_score)/N)

"""
split() 메서드는 리스트를 반환한다

strip() 메서드 { lstrip(), rstrip() }
삭제할 문자를 따로 지정하지 않으면 모든 종류의 blank 문자를 삭제한다
여기서 blank 문자는 스페이스, 탭, 개행문자 등이 있다
"""