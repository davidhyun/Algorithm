def solution(clothes):
    clothes_dict = {}
    for value, key in clothes:
        clothes_dict.setdefault(key, []).append(value)

    answer = 1
    for key in clothes_dict.keys():
        # (a + 1)(b + 1)(c + 1) - 1 = (a + b + c) + (ab + bc + ca) + abc
        # (모자 개수 + 1) * (안경 개수 + 1) * (신발 개수 + 1)
        answer = answer * (len(clothes_dict[key]) + 1)

    return answer - 1 # 모두 안입는 경우는 없으니 최종 경우의 수에서 -1


def solution2(clothes):
    from collections import Counter
    each_key_count = Counter([key for _, key in clothes])

    answer = 1
    for key in each_key_count:
        # (a + 1)(b + 1)(c + 1) - 1 = (a + b + c) + (ab + bc + ca) + abc
        # (모자 개수 + 1) * (안경 개수 + 1) * (신발 개수 + 1)
        answer *= (each_key_count[key] + 1)

    return answer - 1 # 모두 안입는 경우는 없으니 최종 경우의 수에서 -1


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))