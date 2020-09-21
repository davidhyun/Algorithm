# 방법1
S = input()
alpha = "abcdefghijklmnopqrstuvwxyz"

for i in alpha:
    print(S.find(i), end=" ")


# 방법2
S = input()
alpha_set = set(S) # 중복제거는 무조건 set(), 단 순서 없이 저장

alpha_list = [-1 for _ in range(26)]
for alpha in alpha_set:
    index = ord(alpha) - ord('a')
    alpha_list[index] = S.find(alpha)
print(*alpha_list)


#방법3
S = input()
print(*[S.find(chr(i+97)) for i in range(26)])

"""
String.find("a") # 문자열 중 찾는 문자가 처음으로 나온 위치(index)를 반환하고 찾고자하는 문자나 문자열이 없으면 -1을 반환
String.index("a") # 문자열 중 찾는 문자가 처음으로 나온 위치(index)를 반환하지만 없으면 오류를 발생

# 파이썬에서 문자와 아스키코드간 변환
ord("문자") : 문자를 아스키코드 숫자로 변환, ord("a")=97, ord("A")=65
chr(숫자) : 숫자에 해당하는 아스키코드 문자로 변환
"""