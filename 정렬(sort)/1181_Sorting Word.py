import sys

T = int(sys.stdin.readline())
l = []
for _ in range(T):
    word = sys.stdin.readline().replace("\n", "")
    word_len = len(word)
    l.append((word, word_len))

for x in sorted(list(set(l)), key=lambda x: (x[1], x[0])):
    print(x[0])

"""
# iterable은 각각의 요소를 하나씩 차례로 반환할 수 있는 객체 (list tuple str set dict range)
# iterator는 순회하면서 다음 데이터를 불러올 수 있는 객체
# sequence는 순서가 있고 순회가 가능하다 (str, tuple, list)

# iterable object는 iterator인가? 반드시 그렇지는 않다
# list는 iterable 하지만, next() 메서드로 호출해도 동작하지 않는다. 즉 iterator가 아니다

s = set([1,2,3]) # set(1 argument), append 사용불가
s.add(4)
s.update([5,6,7])
s.remove(3)
"""