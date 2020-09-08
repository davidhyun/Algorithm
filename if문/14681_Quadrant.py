#x, y = map(int, input().split())

x = int(input("x좌표 입력:"))
y = int(input("y좌표 입력:"))

if x > 0 and y > 0:
    print("1사분면")
elif x < 0 and y > 0:
    print("2사분면")
elif x < 0 and y < 0:
    print("3사분면")
elif x > 0 and y < 0:
    print("4사분면")

"""
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
"""
