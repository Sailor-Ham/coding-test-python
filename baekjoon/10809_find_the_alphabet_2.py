# 백준 10809 - 알파벳 찾기

import sys

input = sys.stdin.readline

result = []
string = input().rstrip()

for i in range(ord("a"), ord("z") + 1):
    result.append(string.find(chr(i)))

print(*result)
