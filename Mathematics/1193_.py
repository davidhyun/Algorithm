N = int(input())

i = 1
j = 1
k = 1
flag = True
while True:
    if k == N:
        print(str(i/j))
        break
    elif flag == True:
        j += 1
        k += 1
        flag = False
    elif flag == False:
        i += 1
        k += 1
        flag = True