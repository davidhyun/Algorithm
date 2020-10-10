##### 선형리스트 #####
# 빈 배열 준비
katok = []

# 배열 제일 뒤에 친구 추가하는 함수
def add_data(friend):
    katok.append(None) # 빈칸 추가
    kLen = len(katok) # 배열의 길이
    katok[kLen-1] = friend

add_data("다현")
add_data("정연")
add_data("쯔위")
print(katok) # ['다현', '정연', '쯔위']

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1] # 밀기
        katok[i-1] = None # 이동된 데이터 자리 비워주기
    katok[position] = friend

insert_data(1, "사나")
print(katok) # ['다현', '사나', '정연', '쯔위']

def delete_data(position):
    kLen = len(katok)
    katok[position] = None
    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1]) # 자리 삭제

delete_data(2)
print(katok) # ['다현', '사나', '쯔위']
