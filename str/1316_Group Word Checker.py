N = int(input())

group_word = [] # 그룹단어가 들어가는 리스트
for _ in range(N):
    string = input()
    storage = [] # 다음 문자와 비교하여 다르면 현재 인덱스의 문자가 들어가는 저장소
    try:
        for i in range(len(string)):
            if string[i] in storage:
                #print("그룹단어 아니다")
                break
            else:
                if string[i] == string[i+1]:
                    continue
                elif string[i] != string[i+1]:
                    storage.append(string[i])
    except IndexError:
        #print("그룹단어이다")
        group_word.append(string)
print(len(group_word))

"""
# 방법1
a[i] 와 a[i+1]을 비교할 때 for문을 돌다보면 i+1때문에 IndexError가 뜰테지만
pre="" or pre=0 으로 초기화해주고 이전 값과 현재값을 비교하면 for문에서 IndexError가 뜨지 않을 것이다.

# 방법2
N = int(input())

result = 0
for _ in range(N):
    word = input()
    ['h', 'a', 'p', 'p', 'y'], ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'a']
    ['0', '1', '2', '2', '3'], ['0', '0', '2', '2', '2', '5', '5', '0']
    if list(word) == sorted(word, key=word.find): # key는 정렬방식(함수도 가능)
        result += 1
print(result)
"""