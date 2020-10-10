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