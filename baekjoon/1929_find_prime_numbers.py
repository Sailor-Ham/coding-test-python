import sys
import math

read = sys.stdin.readline
sqrt = math.sqrt

M, N = map(int, read().split())

for n in range(M, N + 1):

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            break
    else:
        print(n)