import sys

S = sys.stdin.readline().replace("\n", "")

l=[]
for i in range(len(S)):
    l.append(S[i])

l_sorted = sorted(l, key=lambda x: -int(x))
print("".join(l_sorted))

"""
s = "2143"
print(sorted("2143")) # ['1', '2', '3', '4']

print("".join(sorted(input())[::-1]))
"""