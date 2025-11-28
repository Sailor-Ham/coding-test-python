# 백준 10872 - 팩토리얼

# TODO: 블로그 작성해야 함
# 딱히 어려운 부분이 아예 없었으므로
# factorial의 구조 및 풀이만 작성

import sys

read = sys.stdin.readline


# 팩토리얼 함수
def factorial(n):
    # 탈출 조건
    if n <= 1:
        return 1

    return n * factorial(n - 1)


n = int(read())

print(factorial(n))
