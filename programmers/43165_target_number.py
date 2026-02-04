# 프로그래머스 43165 - 타겟 넘버

def solution(numbers, target):
    def get_all_sum_plus_or_minus(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0

        return (get_all_sum_plus_or_minus(index + 1,
                                          current_sum + numbers[index]) +
                get_all_sum_plus_or_minus(index + 1,
                                          current_sum - numbers[index]))

    return get_all_sum_plus_or_minus(0, 0)


numbers_1 = [1, 1, 1, 1, 1]
target_1 = 3

numbers_2 = [4, 1, 2, 1]
target_2 = 4

print("기대: 5, 정답:", solution(numbers_1, target_1))
print("기대: 2, 정답:", solution(numbers_2, target_2))
