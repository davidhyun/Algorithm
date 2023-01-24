import collections


def solution_my(participant, completion):
    # O(n)
    p = collections.Counter(participant)
    c = collections.Counter(completion)
    
    answer = set(p - c).pop()
    return answer
    
    
def solution_ref1(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
    
    
if __name__ == "__main__":
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "mislav", "ana"]
    
    print(solution_my(participant, completion))
    print(solution_ref1(participant, completion))