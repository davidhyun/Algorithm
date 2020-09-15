import sys

N = int(sys.stdin.readline())

element = list(map(int, sys.stdin.readline().split())) # map함수로 여러개 요소들에 동일 규칙을 적용하여 받은 인수를 list()로 묶는다
#print(element)
#print(*element) # unpacking
print(min(element), max(element))

"""
# iterable 객체는 member를 하나씩 차례로 반환 가능한 object
# iterable obj(sequence type : list, tuple, str)

map_obj = map(int, sys.stdin.readline().split())
print(map_obj)
print(*map_obj) # unpacking
"""