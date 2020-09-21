import sys

N = int(sys.stdin.readline())
string_number = int(sys.stdin.readline())

sum = 0
for x in str(string_number):
    sum += int(x)
print(sum)

"""
# map 함수는 일괄적용하고 싶을때 map(적용하고자하는 함수, iterable객체)
# 리턴되는 것은 map 객체

N = int(input())
print(sum(map(int, input())))
"""
