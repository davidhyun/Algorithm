import sys

for line in sys.stdin:
    if line == ".\n": break

    stk = []
    flag = True
    for x in line:
        if x == "(" or x == "[":
            stk.append(x)

        elif x == ")":
            if not stk or stk[-1] == "[":
                flag = False
                break
            elif stk[-1] == "(":
                stk.pop()

        elif x == "]":
            if not stk or stk[-1] == "(":
                flag = False
                break
            elif stk[-1] == "[":
                stk.pop()

    if flag == True and not stk:
        print("yes")
    else:
        print("no")
