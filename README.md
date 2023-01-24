# 코딩테스트

- 코딩테스트의 목적 : **기본적인** 구현 능력과 문제 해결 능력의 검증
  - 구현 능력 : 기본적인 언어 문법, 자료구조, 알고리즘, 문자열 처리 능력
  - 문제해결 능력 : 문제를 제대로 이해하고 효율적으로 해결하는 능력
- 복잡한 알고리즘이 아닌, 필수적인 자료구조와 알고리즘을 활용할 수 있는지 판단
- 코딩테스트는 1등이 아닌 pass가 목표

<br/>

## 1. 알고리즘/자료구조

### 1.1 알고리즘

- 문제를 해결하기 위한 방법론
- `Brute-Force`, `Binary-Search`, `DFS`, `BFS`, `Backtracking`, `DP`, `Greedy`, `순열조합`

### 1.2 자료구조

- Computer Science(CS)에서 효율적인 데이터 접근 및 수정을 가능하게 하는 자료의 조직, 관리, 저장을 의미
- `Stack`, `Queue`, `Deque`, `Hash`, `Graph`, `Heap`, `Tree`

<br/>

## 2. 알고리즘 평가기준

### 2.1 시간복잡도(Big-O)

코드를 수행함에 있어서 적은 시간이 드는 알고리즘일 수록 좋다. 동일한 코드로 작성되어도 실행 환경에 따라 매번 실행시간(runtime)이 달라질 수 있다. 하지만 시간 스케일을 계산할 수 있고, 이러한 시간복잡도를 Big-O로 표기한다.

![image](https://user-images.githubusercontent.com/64063767/214215405-d5bf3d80-a55b-463b-84e4-42d66a8f0d7a.png)

```python
# O(1), simple statements
a = 5
a += 1

# O(n), single loop
for i in range(n):
  print("hi")
  
# O(n^2), nested loop
for i in range(n):
  for j in range(n):
    print(i*j)
    
# O(2^n), twice call recursion
def recursion(n):
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return recursion(n-1) + recursion(n-2)
  
# O(logn), binary search
def binarySearch(list, n, target):
  start = 0
  end = n
  
  while end >= start:
    mid = (start+end)/2
    if list[mid] == target:
      return 1
    elif list[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  
  return 0
```

- 정렬(sort) : O(nlogn)
- Hashtable 구축 : O(n)
- Hashtable 검색 : O(1)
- Heap
  - 길이가 n인 배열을 heap으로 만들 때 : O(nlogn)
  - push() : O(logn)
  - pop() : O(logn)

<br/>

### 2.2 공간복잡도(Memory)

메모리는 한정적이기 때문에 적은 용량의 메모리를 사용하는 것이 좋다. 하지만 컴퓨터 하드웨어의 발전에 따라 메모리를 크게 신경쓰지 않고 알고리즘을 작성하는 경우도 있다.

<br/>

### 2.3 구현 복잡도

개발자는 협업을 하는 경우가 많으므로 구현이 너무 복잡해지면 다른 사람은 물론 자신도 알아보기 어려워질 수 있다. 직관적이고 이해하기 쉬운 코드 설계를 지향해야한다.

<br/>

시간과 공간복잡도는 보통 trade-off 관계이다. 꼭 그렇지는 않지만 실행시간을 줄이려면 메모리를 더 사용해야하고, 메모리 사용량을 줄이려면 실행시간이 늘어나게된다.

또한, 실행시간이 적게 걸리고, 메모리를 적게 차지하는 알고리즘이 무조건 좋은 것은 아니다. 복잡한 알고리즘은 개발시간이 늘어날 수 있기 때문에 시간과 공간을 좀 더 차지하더라도 직관적이고 이해하기 쉬운 코드를 작성하는 편이 더 나을 수 있다. 따라서 시간복잡도와 공간복잡도를 미리 계산하여 요구상황에 맞는, 직관적인 알고리즘을 사용하는 것이 중요하다.

<br/>

## 3. References

- [시간복잡도](https://www.nossi.dev/cote/time-complexity)

- [현업 엔지니어의 시각에서 본 알고리즘 공부의 장점과 단점](https://www.slideshare.net/wonharyu/ss-62184255)

