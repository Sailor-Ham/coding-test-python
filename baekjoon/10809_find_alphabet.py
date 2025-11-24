# 백준 10809 - 알파벳 찾기

import sys

read = sys.stdin.readline

value = read().rstrip()

alphabet_array = [-1] * 26
index = 0

for char in value:
    if alphabet_array[ord(char) - ord('a')] != -1:
        index += 1
        continue

    alphabet_array[ord(char) - ord('a')] = index

    index += 1

print(*alphabet_array)