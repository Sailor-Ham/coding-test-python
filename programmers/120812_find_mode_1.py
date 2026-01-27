# 프로그래머스 120812 - 최빈값 구하기
# 최초 풀이

def solution(array):
    if len(array) == 1:
        return array[0]

    count_dict = {}

    for num in array:
        count_dict[num] = count_dict.get(num, 0) + 1

    if len(count_dict) == 1:
        return array[0]

    max_count = 0

    for ele in count_dict:
        current_occur = count_dict.get(ele)

        if current_occur > max_count:
            max_count = current_occur

    flag = False
    mode = 0

    for ele in count_dict:
        current_occur = count_dict.get(ele)

        if current_occur == max_count:
            if flag:
                return -1

            mode = ele
            flag = True

    return mode


array1 = [1, 2, 3, 3, 3, 4]
array2 = [1, 1, 2, 2]
array3 = [1]

print("정답: 3, 내가 푼 답:", solution(array1))
print("정답: -1, 내가 푼 답:", solution(array2))
print("정답: 1, 내가 푼 답:", solution(array3))
