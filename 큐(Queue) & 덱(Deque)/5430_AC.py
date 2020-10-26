import sys
import re

def AC(commands, n, arr):
    """
    명령어마다 pop을 시키지 않고 한번에 명령어를 수행할 수 있도록한다
    R과 D 명령어에 따라서 왼쪽에서 몇 개를 지우고 오른쪽에서 몇개를 지울지 숫자를 센 후 한번에 지워준다
    """
    commands.replace("RR", "")
    l, r, left = 0, 0, True # l, r = 왼쪽과 오른쪽의 지워줄 개수, left = False(reversed)

    for com in commands:
        if com == "R":
            left = not left
        elif com == "D":
            if left:
                l += 1
            else:
                r += 1

    if l + r <= n:
        result = arr[l:n-r]
        if left:
            return '[' + ','.join(result) + ']'
        else:
            return '[' + ','.join(result[::-1]) + ']'
    else:
        return "error"


T = int(sys.stdin.readline())
for _ in range(T):
    commands = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = re.findall("\d+", sys.stdin.readline()) # str
    # arr = sys.stdin.readline().rstrip()[1:-1].split(',') # str
    if n == 0: arr=[]
    print(AC(commands, n, arr))

"""
eval() 입력받은 문자열 그대로를 똑같이 쓰겠다 # 시간이 엄청소요(비추)
a = 2
b = 3
s = "a+b"
print(eval(s))
"""