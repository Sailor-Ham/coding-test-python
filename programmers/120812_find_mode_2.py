# 프로그래머스 120812 - 최빈값 구하기
# max() 내장 함수와 리스트 컴프리헨션 기능 활용

def solution(array):
    count_dict = {}

    for num in array:
        count_dict[num] = count_dict.get(num, 0) + 1

    # 최빈값을 max() 내장 함수 사용하여 구함
    max_count = max(count_dict.values())

    # 리스트 컴프리헨션 기능 사용
    modes = [num for num, count in count_dict.items() if count == max_count]

    if len(modes) > 1:
        return -1
    else:
        return modes[0]


array1 = [1, 2, 3, 3, 3, 4]
array2 = [1, 1, 2, 2]
array3 = [1]

print("정답: 3, 내가 푼 답:", solution(array1))
print("정답: -1, 내가 푼 답:", solution(array2))
print("정답: 1, 내가 푼 답:", solution(array3))
