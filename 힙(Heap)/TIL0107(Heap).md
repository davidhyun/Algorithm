# Heap

> **데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)**
>
> 완전 이진 트리: 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리
>



### (1) Heap을 사용하는 이유

- 배열에 데이터를 넣고, 최대값과 최소값을 찾으려면 O(n)이 걸림
- 이와 달리, Heap에 데이터를 넣고 최대값과 최소값을 찾으면 **O(logn)**이 걸림
- 우선순위 큐와 같이 **최대값 또는 최소값을 빠르게 찾아야하는 자료구조 및 알고리즘 구현에 활용**



### (2) Heap의 동작 (Max Heap의 예시)

| Heap에 데이터 삽입                                           | Heap의 데이터 삭제                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![힙에 데이터 삽입](https://user-images.githubusercontent.com/64063767/103858913-83e90800-50fc-11eb-9af9-70bc66b6c325.png) | ![힙의 데이터 삭제](https://user-images.githubusercontent.com/64063767/103858916-851a3500-50fc-11eb-9986-11904f776011.png) |



### (3) Heap 생성, 원소추가 및 삭제 (Default::Min Heap)

- https://www.daleseo.com/python-heapq/
- min heap을 사용하면 원소들이 항상 정렬된 상태로 추가되고 삭제되며, min heap에서 가장 작은 값은 언제나 첫번째 인덱스, 즉 이진 트리의 root node에 위치한다.

```python
import heapq

heap = []
heapq.heapify(heap) # 이미 원소가 들어있는 리스트도 힙으로 만들 수 있다. 
					# 이 경우, 비어있는 리스트에 heappush() 함수로 원소를 하나씩 추가한 것과 동일하다. 
        			# 이 때 리스트의 원소 수에 비례하는 O(n) 시간 복잡도를 가진다.

# Heap에 원소 추가
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap) # [1, 3, 7, 4]

# Heap의 원소 삭제
heapq.heappop(heap) # 1
print(heap) # [3, 4, 7]

# 최소값 삭제 없이 최소값 읽기
print(heap[0])
```



### (4) Max Heap

- heapq 모듈은 최소 힙(min heap)이 default이기 때문에 최대 힙(max heap)을 사용하려면 힙에 튜플을 원소로 추가하거나 삭제하여 튜플 내에서 맨앞에 있는 값을 기준으로 힙을 구성하면 최대힙을 만들 수 있다.

- 최대 힙을 만들려면 각 값에 대한 우선순위를 구한후, `(우선순위, 값)` 튜플을 힙에 추가하거나 삭제하면 된다.
- 최대 힙에서 값을 읽어올 때는 튜플에서 두번째있는 값을 읽으면 된다. 

```python
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
    heapq.heappush(heap, (-num, num)) # (우선순위, 값)
    
while heap:
    print(heapq.heappop(heap)[1])
    
>>> 8
>>> 7
>>> 5
>>> 4
>>> 3
>>> 1
```



### (5) k번째 최소값/최대값

```python
import heapq

def kth_smallest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        
    kth_min = None
    # k번째 최소값을 구하기 위해 heappop() 함수를 k번 호출
    for _ in range(k):
        kth_min = heapq.heappop(heap)
        
    return kth_min

print(kth_smallest([4,1,7,3,8,5], 3)) # 4
```



### (6) Heap Sorting

```python
import heapq

def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        
    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
        
    return sorted_nums

print(heap_sort([4,1,7,3,8,5])) # [1, 3, 4, 5, 7, 8]
```



### (7) 주의사항

![heap and binary search tree](https://user-images.githubusercontent.com/64063767/103858235-55b6f880-50fb-11eb-9d3d-f1647d00de3b.png)

- heap의 첫번째 인덱스(root node)에 가장 작은(큰) 값이 있다고해서, 두번째, 세번째 인덱스에 두번째, 세번째 작은(큰) 값이 있다는 보장은 할 수 없다. `heappop()`, `heappush()` 함수를 호출하여 원소를 추가하고 삭제할 때마다 이진 트리를 재배치하고 매번 새로운 최소값을 첫번째 인덱스로 위치시킨다. 이는 탐색을 위한 이진 탐색 트리(Binary Search Tree) 구조와는 달리 힙(Heap)은 최대/최소값 검색을 위한 구조이기 때문이다.



### (8) Heap 클래스 생성

- https://www.fun-coding.org/Chapter11-heap.html

```python
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None) # 인덱스 번호는 1번부터
        self.heap_array.append(data)

        
    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        if left_child_popped_idx >= len(self.heap_array):
            return False
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

                
    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1
            if right_child_popped_idx >= len(self.heap_array):
                self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                popped_idx = left_child_popped_idx
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
                else:
                    self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
                    popped_idx = right_child_popped_idx

        return  returned_data

    
    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

        
    def insert(self, data):
        if len(self.heap_array) == 1:
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx

        return True
```

