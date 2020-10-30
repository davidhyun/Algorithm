### Class ###
import sys

class Deque:
    def __init__(self):
        self.deq = []
    def push_front(self,num):
        self.deq.insert(0, num)
    def push_back(self,num):
        self.deq.append(num)
    def pop_front(self):
        print(self.deq.pop(0) if self.deq else -1)
    def pop_back(self):
        print(self.deq.pop() if self.deq else -1)
    def size(self):
        print(self.deq.__len__())
    def isempty(self):
        print(0 if self.deq else 1)
    def front(self):
        print(self.deq[0] if self.deq else -1)
    def back(self):
        print(self.deq[-1] if self.deq else -1)

# 해당 모듈이 import된 경우가 아니라 인터프리터에서 직접 실행된 경우에만 if문 이하의 코드블럭을 수행하라
# (모듈에서 import해서 실행하면 __name__ 변수에 모듈명.py의 모듈명이 담겨서 프린트된다)
if __name__ == "__main__":
    deq = Deque() # 클래스 객체 생성
    T = int(sys.stdin.readline())
    for _ in range(T):
        command = sys.stdin.readline().strip().split()
        if command[0] == "push_front":
            deq.push_front(command[1])
        elif command[0] == "push_back":
            deq.push_back(command[1])
        elif command[0] == "pop_front":
            deq.pop_front()
        elif command[0] == "pop_back":
            deq.pop_back()
        elif command[0] == "size":
            deq.size()
        elif command[0] == "empty":
            deq.isempty()
        elif command[0] == "front":
            deq.front()
        elif command[0] == "back":
            deq.back()
