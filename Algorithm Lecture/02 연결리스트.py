##### 연결리스트 #####
class Node:
    def __init__(self):
        self.data = None
        self.link = None

def printNode(current):
    print(current.data, end = " --> ")
    while current.link != None:
        current = current.link
        print(current.data, end = " --> ")
    print()


node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

node3 = Node()
node3.data = "쯔위"
node2.link = node3
print(node1.data, node1.link.data, node1.link.link.data, sep=" --> ") # 다현 --> 정연 --> 쯔위

newNode = Node()
newNode.data = "재남"
newNode.link = node2.link
node2.link = newNode
print(node1.data, node1.link.data, node1.link.link.data, node1.link.link.link.data, sep=" --> ") # 다현 --> 정연 --> 재남 --> 쯔위

current = node1
print(current.data, end = " --> ")
while current.link != None:
    current = current.link
    print(current.data, end = " --> ") # 다현 --> 정연 --> 재남 --> 쯔위 -->
print()

# 재남 노드(newNode)를 삭제
node2.link = node3
del(newNode)

printNode(node1) # 다현 --> 정연 --> 쯔위 -->
