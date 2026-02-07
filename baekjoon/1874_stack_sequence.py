# 백준 1874 - 스택 수열

import sys

input = sys.stdin.readline

N = int(input())
targets = []
for _ in range(N):
    targets.append(int(input()))

stack = []
result = []

cur = 1
is_possible = True

for target in targets:
    while cur <= target:
        stack.append(cur)
        result.append("+")
        cur += 1

    if stack and stack[-1] == target:
        stack.pop()
        result.append("-")
    else:
        is_possible = False
        break

if is_possible:
    print("\n".join(result))
else:
    print("NO")
