# 백준 1439 - 뒤집기

import sys

input = sys.stdin.readline

string = input().rstrip()

count_to_all_zero = 0
count_to_all_one = 0

if string[0] == "1":
    count_to_all_zero += 1
else:
    count_to_all_one += 1

for idx in range(len(string) - 1):
    curr = string[idx]
    next = string[idx + 1]

    if curr != next:
        if next == "1":
            count_to_all_zero += 1
        else:
            count_to_all_one += 1

print(min(count_to_all_zero, count_to_all_one))
