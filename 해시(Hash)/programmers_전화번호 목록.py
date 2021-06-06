from itertools import combinations

# 시간초과
def solution1(phone_book):
    answer = True
    phone_book.sort(key=len)
    comparison_factor = combinations(phone_book, 2) # iterable

    hash_table = {}
    for key, value in comparison_factor:
        hash_table.setdefault(key, []).append(value)

    print(hash_table)
    for key, value_list in hash_table.items():
        for value in value_list:
            if value.startswith(key):
                answer = False
                return answer

    return answer


def solution2(phone_book):
    phone_book.sort() # 인접요소만 확인하도록 정렬하여 시간단축

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return True

phone_book = ['119', '97674223', '1195524421']
# phone_book = ['123', '456', '789']
# phone_book = ['12', '123', '1235', '567', '88']
# phone_book = ['1989', '27723', '299235', '5252367', '8234131138', '198923498249']

print(solution2(phone_book))