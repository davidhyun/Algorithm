import sys

N = int(sys.stdin.readline())

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    alpha = set()
    alpha.add(word[0])
    pre = word[0] # 더미변수

    for s in word:
        if pre == s:
            continue
        else:
            if s in alpha:
                N -= 1
                break
            else:
                alpha.add(s)
                pre = s

print(N)