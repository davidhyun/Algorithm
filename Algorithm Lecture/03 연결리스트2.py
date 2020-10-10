### 함수 선언부 ###
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


def insert_node(findData, insertData):
    global head, pre, current
    # 입력할 데이터가 제일 처음이될 때
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return

    # 입력데이터가 중간에 있을 때
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return

    # 찾는 데이터가 없을 때
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)


### 전역 변수부 ###
memory = []
head, current, pre = None, None, None # 시작노드, 현재노드, 앞노드
dataAry = ["다현", "정연", "쯔위"]


### 메인 코드부 ###
if __name__ == "__main__":
    node = Node()
    node.data = dataAry[0]
    head = node
    memory.append(node)

    for data in dataAry[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNode(head) # 다현 --> 정연 --> 쯔위 -->
    insert_node("다현", "화사"); printNode(head) # 화사 --> 다현 --> 정연 --> 쯔위 -->
    insert_node("쯔위", "재남"); printNode(head) # 화사 --> 다현 --> 정연 --> 재남 --> 쯔위 -->
    insert_node("없다", "막내"); printNode(head) # 화사 --> 다현 --> 정연 --> 재남 --> 쯔위 --> 막내 -->

