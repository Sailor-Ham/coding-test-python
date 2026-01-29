# 백준 1929 - 소수 구하기

import sys

input = sys.stdin.readline

M, N = map(int, input().split())

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for num in range(2, int(N ** 0.5) + 1):
    if is_prime[num]:
        for multiple in range(num * num, N + 1, num):
            is_prime[multiple] = False

for num in range(M, (N + 1)):
    if is_prime[num]:
        print(num)
