# 백준 10872 - 팩토리얼

import sys

input = sys.stdin.readline


def factorial(n):
    if n < 1:
        return 1

    return n * factorial(n - 1)


N = int(input())

print(factorial(N))
