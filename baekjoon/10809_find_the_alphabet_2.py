# 백준 10809 - 알파벳 찾기

import sys

input = sys.stdin.readline

result = []
string = input().rstrip()

# 97 ~ 123(122 + 1)까지 26번 반복
for i in range(ord("a"), ord("z") + 1):
    # 내장 함수 find를 활용
    result.append(string.find(chr(i)))

print(*result)
