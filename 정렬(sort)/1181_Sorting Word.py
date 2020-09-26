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
s = set([1,2,3]) # set(1 argument), append 사용불가
s.add(4)
s.update([5,6,7])
s.remove(3)
"""
