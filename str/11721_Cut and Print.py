import sys

s = sys.stdin.readline()

for i in range(0, len(s), 10):
    print(s[i:i+10])

"""
class Student:
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age

    # iterable 객체이지만 클래스 안에 __repr__이 정의되어있어야만 print()함수로 호출 가능
    def __repr__(self):
        repr = (self.name, self.grade, self.age)
        return str(repr)

Student_object = [Student('Messi','A',26), Student('James','B',20), Student('Son','C',25)]
print(Student_object)
"""