import sys

T = int(sys.stdin.readline())

l = []
for _ in range(T):
    l.append(int(sys.stdin.readline()))

print(*sorted(l), sep="\n")
#print(*sorted(target_list, key=lambda x:-x), sep="\n")

"""
# sorted는 기존객체는 보존한채 정렬하여 새로운 객체로 리턴
l = [(1,1), (1,2), (2,5), (2,7), (7,9)]
print(*sorted(l, key=lambda x: (x[0], -x[1])))

m = [("abc", 1), ("asd", 2), ("asdad", 4), ("adfww", 9)]
print(*sorted(m, key=lambda x: (-len(x[0]), -x[1])))
"""
