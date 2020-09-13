"""
Python에서 Null객체는 None으로 표현한다

테스트 케이스의 개수가 주어지지 않았기 때문에
(1) except구문으로 종료를 처리
(2) for문으로 처리(에러 발생)
"""

import sys

# (1) 예외처리구문으로 문제풀이
while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        exit() # break

# (2) for문으로 종료처리
for line in sys.stdin:
    A, B = map(int, line.split())
    print(A+B)
