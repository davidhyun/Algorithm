print(11/3) #3.6
print(11//3) #3, 몫
print(11%3) #2, 나머지

#윤년 X : 1800, 1900, 2100
#윤년 O : 2012, 2000, 2400

year = int(input("연도를 입력하시오 : "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("윤년이다")
else:
    print("윤년이 아니다")

"""
year = int(input())
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("1")
else:
    print("0")
"""