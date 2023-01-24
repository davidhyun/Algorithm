import collections


def solution_my(nums):
    # O(n)
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    
    return min(len(d.keys()), len(nums)//2)

    
def solution_ref1(nums):
    # O(n)
    # Counter type, Not dictionary
    # 카운터 타입은 딕셔너리 타입과 다르게 덧셈 뺄셈이 가능, 하지만 곱셈, 나눗셈, 값이 None일 때는 불가능
    d = collections.Counter(nums)    
    return min(len(d.keys()), len(nums)//2)
    

def solution_ref2(nums):
    # O(n)
    return min(len(set(nums)), len(nums)//2)
    
    

if __name__ == "__main__":
    nums = [3,1,2,3]
        
    print(solution_my(nums))
    print(solution_ref1(nums))
    print(solution_ref2(nums))