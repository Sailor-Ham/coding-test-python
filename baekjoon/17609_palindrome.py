# 백준 17609 - 회문


# abba

# 0     3            1 2
# v     v            v v
# a b b a: True -> a b b a: True -> 0

# 0           6            1       5                2   4                     3 4
# v           v            v       v                v   v                     v v    : False
# s u m m u u s: True -> s u m m u u s: True -> s u m m u u s: False -> s u m m u u s:
#                                                                           ^ ^      : True
#                                                                           2 3

import sys

input = sys.stdin.readline


def check_palindrome(string, start, end):
    while start < end:
        if string[start] != string[end]:
            return False

        start += 1
        end -= 1

    return True


def palindrome(string):
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            if (check_palindrome(string, start + 1, end)
                or check_palindrome(string, start, end - 1)):
                return 1
            else:
                return 2

    return 0


T = int(input())

for _ in range(T):
    print(palindrome(input().rstrip()))
