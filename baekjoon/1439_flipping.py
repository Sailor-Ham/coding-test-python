# 1439 - 뒤집기

# 0001100 - 1회 뒤집기
# 11101101 - 2회 뒤집기

# 1 -> 0 전부 0으로 만드는 방법
# 0 -> 1 전부 1로 만드는 방법

# 0001100

# 만약 전부 1로 만들기 위해서는
# 1 ~ 3 -> 1
# 6 ~ 7 -> 1
# 2회

# 만약 전부 0으로 만들기 위해서는
# 4 ~ 5 -> 1
# 1회

# 둘 중에 적은게 최소

import sys

read = sys.stdin.readline

input_string = read().rstrip()

# 각각 0, 1로 뒤집는 횟수
count_to_all_zero = 0
count_to_all_one = 0

# i + 1을 기준으로 작업하므로 맨 처음 i에 대한 판별 작업 수행
if input_string[0] == '0':
    count_to_all_one += 1
elif input_string[0] == '1':
    count_to_all_zero += 1

# i + 1 부터 뒤집히는 횟수 카운트
for i in range(len(input_string) - 1):
    if input_string[i] != input_string[i + 1]:
        if input_string[i + 1] == '1':
            count_to_all_zero += 1
        elif input_string[i + 1] == '0':
            count_to_all_one += 1

print(min(count_to_all_zero, count_to_all_one))