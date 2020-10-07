import sys


class Queue:
    def __init__(self):
        self.items = []

    # enqueue
    def push(self, data):
        self.items.append(data)

    # dequeue
    def pop(self):
        if self.items:
            data = self.items[0] # 내장함수 pop(0)은 꺼내고 리스트를 다시 당겨서 써줘야하기 때문에 시간복잡도 O(n)이 되서 시간 초과로 문제를 해결할 수 없다
            del self.items[0] # del함수를 사용하면 나머지 요소들이 앞으로 땡겨지는데 시간이 걸림. deque의 popleft() 이용
            return data
        else:
            return -1

    def size(self):
        return len(self.items)

    def empty(self):
        return (not self.items) # 비어있으면 True(1), 아니면 False(0)

    def front(self):
        if self.items:
            return self.items[0]
        else:
            return -1

    def back(self):
        if self.items:
            return self.items[-1]
        else:
            return -1


N = int(sys.stdin.readline())

if __name__ == "__main__":
    q = Queue()
    for _ in range(N):
        order = sys.stdin.readline().strip().split()

        if order[0] == "push":
            q.push(order[1])
        elif order[0] == "pop":
            print(q.pop())
        elif order[0] == "size":
            print(q.size())
        elif order[0] == "empty":
            print(q.empty())
        elif order[0] == "front":
            print(q.front())
        elif order[0] == "back":
            print(q.back())

"""
https://medium.com/@chullino/if-name-main-%EC%9D%80-%EC%99%9C-%ED%95%84%EC%9A%94%ED%95%A0%EA%B9%8C-bc48cba7f720
if __name__ == "__main__": 
해당 모듈이 import된 경우가 아니라 interpreter에서 직접 실행된 경우에만, if문 이하의 코드를 돌려라!

모듈을 실행할 수 있는 방법
(1) 직접실행 : interpreter에서 직접 실행하면, __name__ 변수에 "__main__"이 담겨서 출력된다
              __name__ : interpreter가 실행 전에 만들어둔 글로벌 변수
(2) import queue
"""
