def solution(array, commands):
    answer = []
    for com in commands:
        i = com[0]
        j = com[1]
        k = com[2]
        num = sorted(array[i-1:j])[k-1]
        answer.append(num)

    return answer

def solution2(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

array = [1,5,2,6,3,7,4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
print(solution2(array, commands))