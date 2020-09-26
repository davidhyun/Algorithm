import sys

T = int(sys.stdin.readline())

l = []
for _ in range(T):
    l.append(int(sys.stdin.readline()))

#print(*sorted(l), sep="\n")
l.sort()
sys.stdout.write("\n".join(map(str, l))) # sys.stdout.write()는 print()의 자동개행을 억제할 때 사용한다

"""
# 문자열 삽입 join
문자열의 각각의 문자 사이에 ","를 삽입한다
",".join("abcd") # 'a,b,c,d'

join 함수는 리스트나 튜플도 입력받을 수 있다
",".join(['a','b','c','d']) # 'a,b,c,d'
"""