import sys

T = int(sys.stdin.readline())
result = [0] * 10001 # 10001개의 초기화 배열 공간
for _ in range(T):
    result[int(sys.stdin.readline())] += 1 # counting

for i in range(10001):
    if result[i] > 0:
        sys.stdout.write(("%s\n" % i) * result[i])

# 실패소스
"""
실패소스1 (메모리 초과)
"""
import sys

T = int(sys.stdin.readline())
l = []
for _ in range(T):
    l.append(sys.stdin.readline().strip())
l.sort() # 여기서 순회하는데 시간초과, 시간복잡도 O(nlogn)
sys.stdout.write("\n".join(map(str, l)))

""" 
실패소스2 (메모리 초과) 
배열이 하나라도 더 생기면 메모리 초과 이슈가 생길 수 있다
"""
import sys

T = int(sys.stdin.readline())
nums = []
for _ in range(T):
    nums.append(int(sys.stdin.readline()))

d = dict()
for i in range(T):
    if i in nums:
        d[i] = nums.count(i)

bundle = []
for key in d:
    bundle.extend([key] * d[key])
print("\n".join(map(str, bundle)))
