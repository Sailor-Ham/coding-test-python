# 백준 17298 - 오큰수

import sys

input = sys.stdin.readline

N = int(input())

array = list(map(int, input().split()))

stack = []
answer = []

for i in range(N - 1, -1, -1):
    while stack:
        if stack[-1] > array[i]:
            answer.append(stack[-1])
            break
        else:
            stack.pop()

    if not stack:
        answer.append(-1)

    stack.append(array[i])

answer.reverse()
print(*answer)
