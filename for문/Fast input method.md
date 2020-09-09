# input() VS sys.stdin.readline()

### 1. input() 말고 sys.stdin.readline()을 사용하자

> 입출력 속도비교
>
> **sys.stdin.readline()** > raw_input() > input()

```python
# 한줄 입력 받을 때
import sys

num = int(sys.stdin.readline()) # num = int(input())
```



```python
# 여러줄 입력 받을 때
import sys

t = input() # 5
num = [sys.stdin.readline() for i in range(t)] # 1, 12, 123, 1234, 12345
print(num) # ['1\n', '12\n', '123\n', '1234\n', '12345\n']
```



### 2. 재귀함수가 있는 경우, 최대 재귀 깊이를 설정해줘야한다

> 특히 자주 접하는 DFS, BFS 문제의 경우가 그렇다. 파이썬의 재귀 허용 깊이가 깊지 않아서 파이썬에서는 런타임 오류가 뜨는 경우가 있다. 그래서 다음과 같이 재귀 허용 깊이를 수동으로 늘려주는 코드를 상단에 적어줘야 한다.

```python
import sys
sys.setrecursionlimit(10**8) # 10**8까지 늘림
```



### 3. PyPy vs Python3

> PyPy는 쉽게 말해서 파이썬보다 몇배 더 빠르게 개선된 파이썬이라고 생각하면 된다.
>
> 한편, PyPy에서는 `sys.setrecursionlimit(10**8)`이 안먹는다. 즉, 임의로 재귀 호출 깊이를 설정할 수 없다는 것에 주의해야한다.