def solution_ref1(phone_book):
    # 원소 길이를 기준으로 정렬 O(nlogn)
    phone_book.sort(key=len)
    hash_table = {}
    
    # 최소 길이를 저장
    min_len = len(phone_book[0])
    
    for target in phone_book:
        # loop마다 본인 정보를 hash table에 저장
        hash_table[hash(target)] = target

        # 최소 길이부터 +1씩 해서 본인 길이 직전까지 hash table에서 검색
        for i in range(min_len, len(target)):
            try:
                if hash_table[hash(target[0:i])]:
                    return False
            except KeyError:
                continue
                
    return True


def solution_ref2(phone_book):
    answer = True
    hash_map = {}
    
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    
    return answer


def solution_ref3(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1,p2)
        if p2.startswith(p1):
            return False
        
    return True


# if __name__ == "__main__":
#     phone_book = ["12","123","1235","567","88"]
#     phone_book2 = ["123","456","789"]
#     phone_book3 = ["119", "97674223", "1195524421"]
    
#     print(solution_ref1(phone_book))
#     print(solution_ref2(phone_book2))
#     print(solution_ref3(phone_book))
#     print(solution_ref3(phone_book2))
#     print(solution_ref3(phone_book3))