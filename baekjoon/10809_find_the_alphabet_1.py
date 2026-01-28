# 백준 10809 - 알파벳 찾기

import sys

input = sys.stdin.readline

result_array = [-1] * 26
string = input().rstrip()
ascii_a = ord("a")

for idx, char in enumerate(string):
    current_ascii = ord(char) - ascii_a

    if result_array[current_ascii] != -1:
        continue

    result_array[current_ascii] = idx

print(*result_array)
