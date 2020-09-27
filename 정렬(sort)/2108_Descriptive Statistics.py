##### 틀린소스 #####
# import sys
#
# N = int(sys.stdin.readline())
# l = []
# for _ in range(N):
#     l.append(int(sys.stdin.readline()))
#
# # 산술평균
# def mean_fn(l):
#     mean = round(sum(l)/len(l))
#     return mean
#
# # 중앙값
# def median_fn(l):
#     median = sorted(l)[((len(l)+1)//2)-1]
#     return median
#
#
# # 최빈값
# new_l = []
# num_count = [0] * N
# def mode_fn(l):
#     for i in range(len(l)):
#         if l[i] not in new_l:   # 숫자가 new_l에 없으면 숫자를 new_l에 추가하고 카운트 +1
#             new_l.append(l[i])
#             num_count[i] += 1
#         else:                   # 이미 숫자가 new_l에 있으면 카운트만 +1
#             num_count[i] += 1
#
#     mode = new_l[num_count.index(max(num_count))]
#     return mode
#
# # 범위
# def range_fn(l):
#     range = max(l)-min(l)
#     return range
#
#
# stat = [mean_fn(l), median_fn(l), mode_fn(l), range_fn(l)]
# stat = list(map(str, stat))
# print("\n".join(stat))

import sys
from collections import Counter # collections 패키지에서 Counter 모듈(함수) 불러오기

N = int(sys.stdin.readline())

numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))


def mean(nums):
    return round(sum(nums) / len(nums))


def median(nums):
    nums.sort()
    mid = nums[len(nums) // 2]  # nums의 개수는 홀수
    return mid


def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()

    if len(nums) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod


def scope(nums):
    return max(nums) - min(nums)


print(mean(numbers), median(numbers), mode(numbers), scope(numbers))


"""
Counter(dict)
>>> c = Counter('abcdeabcdabcaba')  # count elements from a string
Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})

>>> c.most_common(3)                # three most common elements
[('a', 5), ('b', 4), ('c', 3)]

>>> sorted(c)                       # list all unique elements
['a', 'b', 'c', 'd', 'e']

>>> ''.join(sorted(c.elements()))   # list elements with repetitions
'aaaaabbbbcccdde'

>>> sum(c.values())                 # total of all counts
15

>>> c['a']                          # count of letter 'a'
5
"""