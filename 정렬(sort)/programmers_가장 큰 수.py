def solution(numbers):
    str_array = list(map(str, numbers))
    sorted_array = sorted(str_array, key=lambda x: x*3, reverse=True)

    answer = str(int(''.join(sorted_array)))
    return answer

# numbers = [6,10,2]
numbers = [3,30,34,5,9]
# numbers = [0,0,0,0,0]

print(solution(numbers))

"""
문자열 비교연산의 경우 첫번째 문자의 ASCII 코드 숫자로 비교한다.
이때 첫번째 인덱스의 ASCII 코드 숫자가 같으면 다음 인덱스로 넘어가서 비교한다.

배열의 원소값이 1000이하이기 때문에 문자열을 3번 반복하여 다음문자끼리도 비교할 수 있게 만든다. 
"""