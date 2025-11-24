# 프로그래머스 120812 - 최빈값 구하기

def solution(array):

    occurred_dictionary = {}

    for number in array:
        occurred_dictionary[number] = occurred_dictionary.get(number, 0) + 1

    mode_number = 0
    mode_count = 0

    for number, count in occurred_dictionary.items():
        if count > mode_count:
            mode_number = number
            mode_count = count

    for number, count in occurred_dictionary.items():
        if number != mode_number and count == mode_count:
            return -1

    return mode_number

print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))