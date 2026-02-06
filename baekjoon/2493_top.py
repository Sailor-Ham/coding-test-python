# 백준 2493 - 탑

import sys

input = sys.stdin.readline

N = int(input())
stack = []
answer = []

heights = list(map(int, input().split()))

for i in range(len(heights)):
    # 비교 작업
    while stack:
        # 왼쪽이 더 크거나 같아야 함
        if stack[-1][1] >= heights[i]:
            answer.append(stack[-1][0] + 1)
            break

        # 왼쪽이 더 작으면 규칙 위반이므로 삭제해야 함
        else:
            stack.pop()

    # 스택이 비어있다면 수신할 탑이 없음
    if not stack:
        answer.append(0)

    # 현재 탑을 스택에 추가
    stack.append((i, heights[i]))

print(*answer)
