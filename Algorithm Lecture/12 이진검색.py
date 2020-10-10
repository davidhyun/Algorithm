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