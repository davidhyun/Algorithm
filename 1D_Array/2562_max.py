import sys

l = []
for i in range(9):
    l.append(int(sys.stdin.readline()))

print(max(l), l.index(max(l))+1, sep="\n") # list.index(max(list)) 최대값의 인덱스

"""
l = [int(input()) for i in range(9)] # list comprehension
print(max(l), l.index(max(l))+1)
"""
