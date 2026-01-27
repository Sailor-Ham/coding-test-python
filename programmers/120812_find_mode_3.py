# 프로그래머스 120812 - 최빈값 구하기
# collections.Counter 기능 사용

from collections import Counter  # collections 모듈의 Counter 클래스 사용


def solution(array):
    counts = Counter(array)

    # most_common: 빈도수 높은 순으로 정렬
    # e.g., [1, 2, 3, 3, 3, 4] -> [(3, 3), (1, 1), (2, 1), (4, 1)]
    mode_data = counts.most_common()

    # 원소가 1개이거나 첫 번째와 두 번째의 빈도수가 다른 경우 첫 번째가 최빈값
    if len(mode_data) == 1 or mode_data[0][1] != mode_data[1][1]:
        return mode_data[0][0]
    else:
        return -1


array1 = [1, 2, 3, 3, 3, 4]
array2 = [1, 1, 2, 2]
array3 = [1]

print("정답: 3, 내가 푼 답:", solution(array1))
print("정답: -1, 내가 푼 답:", solution(array2))
print("정답: 1, 내가 푼 답:", solution(array3))
