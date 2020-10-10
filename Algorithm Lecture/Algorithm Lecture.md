# 2020.10.10(토) Algorithm Lecture

## (0) 자료구조

![자료구조](https://user-images.githubusercontent.com/64063767/95642321-be81db00-0ae2-11eb-8862-d941818d46ce.png)



## (1) 알고리즘 성능분석

### (I) 알고리즘 성능 기준

- 정확성 : 올바른 자료 입력시 유한한 시간 내에 올바른 결과 출력여부
- 명확성 : 알고리즘이 얼마나 이해하기 쉽고 명확하게 작성되었는가
- 수행량 : 일반적인 연산 제외, 알고리즘 특성을 나타내는 중요 연산을 통한 분석속도
- 메모리 사용량
- 최적성



### (II) 공간 복잡도

> 알고리즘을 프로그램으로 실행하여 완료하기까지 필요한 총 저장 공간의 양
>
> 공간 복잡도 = 고정공간 + 가변공간



### (III) 시간 복잡도

> 알고리즘을 프로그램으로 실행하여 완료하기까지의 총 소요시간
>
> 시간 복잡도 = 컴파일 시간 + 실행 시간
>
> 	- 컴파일 시간 : 프로그램마다 거의 고정적인 시간 소요
> 	- 실행 시간 : 컴퓨터의 성능에 따라 달라질 수 있으므로 실제 실행시간 보다는 명령문의 실행 빈도수에 따라 계산
>
> 실행 빈도수의 계산
>
> - 지정문, 조건문, 반복문 내의 제어문과 반환문은 실행시간 차이가 거의 없으므로 하나의 단위시간을 갖는 기본 명령문으로 취급



### (IV) 알고리즘 성능 분석 표기법

- <span style="color:red;">**빅-오 표기법 O(f(n))**</span>

  - 함수의 상한을 나타내기 위한 표기법

    > 최악의 경우에도 g(n)의 수행시간 안에는 알고리즘 수행완료 보장

  - 먼저 실행 빈도수를 구하여 실행 시간 함수를 찾고, 이 함수 값에 가장 큰 영향을 주는 n에 대한 항을 한 개 선택하여 계수는 생략하고 O의 오른쪽 괄호안에 표시

  - 표기 예시 (피보나치 수열) : 피보나치 수열에서 실행 시간 함수는 4n+2이고, 가장 영향이 큰 항은 4n인데, 여기에서 계수 4를 생략하여 O(n)으로 표기

![시간복잡도](https://user-images.githubusercontent.com/64063767/95643322-7f0abd00-0ae9-11eb-96bc-11864f2fed58.png)





## (2) 선형구조

### (I) 순차 자료구조 - 선형리스트

![순차자료구조](https://user-images.githubusercontent.com/64063767/95657003-00476b80-0b4d-11eb-91bf-cc996572c3e4.png)

- 선형리스트 중간에 원소가 삽입되면, **그 이후의 원소들은 한 자리씩 자리를 뒤로 이동**하여 물리적 순서를 논리적 순서와 일치시킴
- 순차자료구조의 문제점
  - 삽입, 삭제 연산 후에 연속적인 물리 주소를 유지하기 위해 <span style="color:red;">**원소들을 이동시키는 추가 작업과 시간이 소요**</span>
  - 순차 자료구조는 배열을 이용해 구현하기 때문에 배열이 갖고 있는 <span style="color:red;">**메모리 사용의 비효율성**</span> 문제를 내포

|                  | 순차자료구조                                                 |
| ---------------- | ------------------------------------------------------------ |
| 메모리 저장 방식 | 메모리의 저장 시작 위치부터 빈자리 없이 자료를 순서대로 연속하여 저장한다. <br/>논리적인 순서와 물리적인 순서가 일치하는 구현방식이다. |
| 연산 특징        | 삽입, 삭제 연산을 해도 빈자리 없이 자료가 순서대로 연속하여 저장된다.<br/> 변경된 논리적인 순서와 저장된 물리적인 순서가 일치한다. |
| 프로그램 기법    | 배열                                                         |

```python
##### 순차리스트 #####
# 빈 배열 준비
katok = []

# 배열 제일 뒤에 친구 추가하는 함수
def add_data(friend):
    katok.append(None) # 빈칸 추가
    kLen = len(katok) # 배열의 길이
    katok[kLen-1] = friend

add_data("다현")
add_data("정연")
add_data("쯔위")
print(katok) # ['다현', '정연', '쯔위']

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1] # 밀기
        katok[i-1] = None # 이동된 데이터 자리 비워주기
    katok[position] = friend

insert_data(1, "사나")
print(katok) # ['다현', '사나', '정연', '쯔위']

def delete_data(position):
    kLen = len(katok)
    katok[position] = None
    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1]) # 자리 삭제

delete_data(2)
print(katok) # ['다현', '사나', '쯔위']
```



### (II) 연결 자료구조 - 연결리스트

![연결자료구조(Node)](https://user-images.githubusercontent.com/64063767/95656983-cc6c4600-0b4c-11eb-8b38-60327c4a7c4b.png)

- 자료의 논리적인 순서와 물리적인 순서가 불일치
  - 각 원소에 저장되어 있는 다음 원소의 주소에 의해 순서가 연결되는 방식 **(물리적인 순서를 맞추기 위한 오버헤드가 발생하지 않음)**
  - 여러 개의 작은 공간을 연결하여 하나의 전체 자료구조를 표현 **(크기 변경이 유연하고 효율적인 메모리 사용)**
- <span style="color:red;">**노드(Node)**</span> : 연결 자료구조에서 하나의 원소를 표현하기 위한 단위 구조 **<원소, 주소>**

|                  | 연결자료구조                                                 |
| ---------------- | ------------------------------------------------------------ |
| 메모리 저장 방식 | 메모리에 저장된 물리적 위치나 물리적 순서와 상관없이, <br/>링크에 의해 논리적인 순서를 표현하는 구현방식이다. |
| 연산 특징        | 삽입, 삭제 연산을 하여 논리적인 순서가 변경되어도,<br/>링크정보만 변경되고 물리적 순서는 변경되지 않는다. |
| 프로그램 기법    | 포인터                                                       |

```python
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
print(node1.data, node1.link.data, node1.link.link.data, sep=" --> ")
# 다현 --> 정연 --> 쯔위

newNode = Node()
newNode.data = "재남"
newNode.link = node2.link
node2.link = newNode
print(node1.data, node1.link.data, node1.link.link.data, node1.link.link.link.data, sep=" --> ") # # 다현 --> 정연 --> 재남 --> 쯔위

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
```



```python
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

    printNode(head) #다현 --> 정연 --> 쯔위 --> 
    insert_node("다현", "화사"); printNode(head) #화사 --> 다현 --> 정연 --> 쯔위 --> 
    insert_node("쯔위", "재남"); printNode(head) #화사 --> 다현 --> 정연 --> 재남 --> 쯔위 -->
    insert_node("없다", "막내"); printNode(head) 
    #화사 --> 다현 --> 정연 --> 재남 --> 쯔위 --> 막내 --> 
```



### (III) 스택 (Last In - First Out)

![Stack(LIFO)](https://user-images.githubusercontent.com/64063767/95658105-1526fd80-0b53-11eb-88b5-d141edccde54.png)

- 순차 자료구조로 구현한 스택의 장·단점

| 장점                   | 단점                                                         |
| ---------------------- | ------------------------------------------------------------ |
| 1차원 배열로 쉽게 구현 | 물리적으로 크기가 고정된 배열을 사용하므로 <span style="color:red;">**스택의 크기 변경이 어려움**</span> |

```python
stack = [None for _ in range(5)]
top = -1 # top의 인덱스(마지막 인덱스)

# push
top += 1; stack[top] = "커피"
top += 1; stack[top] = "녹차"
top += 1; stack[top] = "꿀물"
print(stack) # ['커피', '녹차', '꿀물', None, None]

# pop
print("뽑기 -->", stack[top]) # 뽑기 --> 꿀물
stack[top] = None
top -= 1
print(stack) # ['커피', '녹차', None, None, None]
```



```python
### 함수 선언부 ###
def isStackFull():
    if top == SIZE-1:
        return True
    else:
        return False

def isEmpty():
    if top == -1:
        return True
    else:
        return False

def push(data):
    global stack, top
    if isStackFull():
        print("스택 FULL")
        return
    top += 1
    stack[top] = data

def pop():
    global stack, top
    if isEmpty():
        print("스택이 비어있음")
        return
    #del stack[top] # 값도 공간도 삭제하고 정렬(시간소요)
    result = stack[top]
    stack[top] = None
    top -= 1
    return result


### 전역 변수부 ###
SIZE = 5 # 스택의 사이즈 제한
stack = [None for _ in range(SIZE)]
top = -1 # top의 인덱스(마지막 인덱스)


### 메인 코드부 ###
print(stack) # [None, None, None, None, None]
push(1); push(2); push(3); print(stack) # [1, 2, 3, None, None]
push(4); push(5); push(6); print(stack, "/ top =", top) 
# 스택 FULL, [1, 2, 3, 4, 5] / top = 4

pop(); pop(); pop(); pop(); pop(); pop(); print(stack, "/ top =", top)
# 스택이 비어있음, [None, None, None, None, None] / top = -1

push("abc"); print(stack, "/ top =", top) # ['abc', None, None, None, None] / top = 0
```



### (IV) 큐 (First In - First Out)

#### <span style="color:red;">순차 큐</span>

![Queue(FIFO)](https://user-images.githubusercontent.com/64063767/95659354-6d61fd80-0b5b-11eb-8231-1e47cb6d089d.png)

- 순차 자료구조로 구현한 큐
  - Queue의 크기 = 배열의 크기
  - front : 첫번째 원소의 인덱스 (초기 front = -1)
  - rear : 마지막 원소의 인덱스 (초기 rear = -1)

```python
queue = [None for _ in range(3)]
front = rear = -1

# Enqueue
rear += 1; queue[rear] = "A"
rear += 1; queue[rear] = "B"
rear += 1; queue[rear] = "C"
print(queue)

# Dequeue
front += 1; print(queue[front]); queue[front] = None # A
print(queue, "front =", front, "rear =", rear) # [None, 'B', 'C'] front = 0 rear = 2

front += 1; print(queue[front]); queue[front] = None # B
print(queue, "front =", front, "rear =", rear) # [None, None, 'C'] front = 1 rear = 2

front += 1; print(queue[front]); queue[front] = None # C
print(queue, "front =", front, "rear =", rear) # [None, None, None] front = 2 rear = 2

rear += 1; queue[rear] = "D" # Error
```



- 순차 자료구조로 구현한 큐의 문제점
  - 삽입삭제를 반복하다보면 **<span style="color:red;">비어있는데도 불구하고 <span style="color:blue;">rear = SIZE-1(Index)</span> 상태이므로 포화상태로 인식하고 더 이상 의 삽입을 수행하지 않는다.</span>** 
  - 저장된 원소들을 배열의 앞부분으로 이동시키면 되긴하지만 연산이 복잡하고 효율성이 떨어진다.



#### <span style="color:red;">원형 큐</span>



![Circular Queue](https://user-images.githubusercontent.com/64063767/95659860-02b2c100-0b5f-11eb-9176-f72d8eecace7.png)

- 원형 큐의 구조
  - 초기 공백 상태 : front = rear = 0
  - front와 rear의 위치가 SIZE-1에서 논리적인 다음 자리인 인덱스 0번으로 이동하기 위해서 <span style="color:red;">**나머지 연산자 mod**</span> 이용
  - 공백상태와 포화상태를 구분하기 위해 **front가 있는 자리는 사용하지 않고 항상 빈자리**로 둔다

```python
### 함수 선언부 ###
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear+1) % SIZE == front:
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        return
    rear = (rear+1) % SIZE
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        return
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


### 전역 변수부 ###
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0


### 메인 코드부 ###
enQueue("A"); enQueue("B"); enQueue("C")
print(queue) # [None, 'A', 'B', 'C', None]
enQueue("D")
deQueue(); deQueue(); deQueue()
enQueue("E"); enQueue("F")
print(queue) # ['E', 'F', None, None, 'D']
```



## (3) 정렬

### (I) 선택정렬

![선택정렬(Selection Sort)](https://user-images.githubusercontent.com/64063767/95660317-01cf5e80-0b62-11eb-8e82-9c2b485bb1f4.png)

> **시간복잡도 = O(n^2)**

```python
import random

### 함수 정의부 ###
def findMinPos(ary):
    minIndex = 0
    for i in range(0, len(ary)):
        if ary[minIndex] > ary[i]:
            minIndex = i
    return minIndex


### 전역 변수부 ###
before = [random.randint(100, 999) for _ in range(20)]
after = []


### 메인 코드부 ###
print("정렬 전 -->", before)

for _ in range(len(before)):
    minPos = findMinPos(before)
    after.append(before[minPos])
    del(before[minPos])

print("정렬 후 -->", after)
```



```python
import random

### 함수 정의부 ###
def selectionSort(arr):
    n = len(arr) # n = 4
    for i in range(n-1): # 사이클 3회
        minIndex = i
        for k in range(i+1, n):
            if ary[minIndex] > ary[k]:
                minIndex = k
        # tmp = ary[i] # 임시저장소
        # ary[i] = ary[minIndex]
        # ary[minIndex] = tmp
        ary[i], ary[minIndex] = ary[minIndex], ary[i]

    return ary


### 전역 변수부 ###
ary = [random.randint(100, 999) for _ in range(20)]


### 메인 코드부 ###
print("정렬 전 -->", ary)
ary = selectionSort(ary)
print("정렬 후 -->", ary)
```



### (II) 퀵 정렬

> 정렬할 전체 원소에 대해서 정렬을 수행하지 않고, **기준값(pivot)을 중심으로 왼쪽 부분집합과 오른쪽 부분집합으로 분할하여 정렬**하는 방법 (기준값은 일반적으로 중앙에 위치한 원소를 선택)
>
> 연산속도
>
> 최선의 경우 : pivot에 의해서 원소들이 왼쪽 부분집합과 오른쪽 부분집합으로 정확히 n/2개씩 2등분이 되는 경우가 반복되어 수행 단계수가 최소가 되는 경우
>
> 최악의 경우 : pivot에 의해 원소들을 분할하였을 때 한개와 n-1개로 한쪽으로 치우쳐 분할되는 경우가 반복되어 수행 단계수가 최대가 되는 경우
>
> **평균 시간복잡도 = O(nlogn)**

```python
import random

### 함수 선언부 ###
def quickSort(ary):
    n = len(ary)
    if n <= 1:
        return ary

    pivot = ary[len(ary)//2] # 중간 값을 기준으로
    leftAry, rightAry = [], []
    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)

    return quickSort(leftAry) + [pivot] + quickSort(rightAry)

### 전역 변수부 ###
ary = [random.randint(100, 999) for _ in range(20)] # 같은 값은 없다고 가정


### 메인 코드부 ###
print("정렬 전 -->", ary)
ary = quickSort(ary)
print("정렬 후 -->", ary)
```



## (4) 재귀호출

- 함수는 호출할 때 Stack 방식을 사용한다

```python
# 함수는 호출할 때 Stack 방식을 사용한다
def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1

    return n * factorial(n-1)

print(factorial(5)) # 120
```



## (5) 검색

### (I) 순차검색 (Sequential Search)

### (II) 이분검색 (Binary Search)

- **성능 최고**, 검색 효율이 최고지만 **정렬이 먼저** 되어있어야 한다

```python
### 함수 정의부 ###
def binarySearch(ary, data):
    start = 0
    end = len(ary) - 1
    while start <= end:
        mid = (start + end) // 2
        if data == ary[mid]:
            return mid
        elif data > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1

### 전역 변수부 ###
dataAry = [1,2,3,4,9,11,66,77,88,128,444,9999]


### 메인 코드부 ###
print(binarySearch(dataAry, 9)) # 4
print(binarySearch(dataAry, 1234)) # -1
```

