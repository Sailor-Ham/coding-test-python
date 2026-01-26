# 백준 2562 - 최댓값

import sys

read = sys.stdin.readline
INPUT_SIZE = 9

numbers = []
for _ in range(INPUT_SIZE):
    numbers.append(int(read()))

max_num = 0
max_index = 0
current_index = 0

for num in numbers:
    if num > max_num:
        max_num = num
        max_index = current_index

    current_index += 1

print(max_num)
print(max_index + 1)
