# 백준 17609 - 회문


# TODO: 블로그 작성해야 함
# 유사 회문을 찾는 과정 설명
# 런타임 에러의 원인
# 런타임 에러를 해결하기 위한 방법
#       문자열의 길이가 최대 10만 => 재귀가 수 만 번 돔
#       파이썬의 기본 재귀 한도: 1천번
#       RecursionError 방지를 위해 재귀 한도를 20만으로 늘림

#       문자열 슬라이싱(string[1:-1])로 작성했으나 작업 과정에서 시간 초과, 메모리 초과 에러 발생하므로
#       인덱스 숫자로만 비교


# 회문: 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열 = 0
# 유사회문: 한 문자를 삭제하여 회문으로 만들 수 있는 문자열 = 1
# 일반 문자열: 회문, 유사 회문이 아닌 문자열 = 2


import sys

# 런타임 에러 발생으로 재귀 함수의 제한을 늘리기로 함
sys.setrecursionlimit(200000)
read = sys.stdin.readline


# 유사 회문 검사 함수
def is_pseudo_palindrome(string, left, right):
    while left <= right:
        if string[left] != string[right]:
            return False
        else:
            left += 1
            right -= 1

    return True


# 회문 검사 함수
def palindrome(string, left, right, is_skipped):
    if left >= right:
        if is_skipped:
            return 1
        else:
            return 0

    if string[left] == string[right]:
        return palindrome(string, left + 1, right - 1, is_skipped)
    else:  # string[0] != string[-1]

        if is_skipped:
            return 2
        else:
            # 한 번의 기회 더 줌 (유사 회문)
            check_left = is_pseudo_palindrome(string, left + 1, right)
            check_right = is_pseudo_palindrome(string, left, right - 1)

            # 둘 중에 하나라도 True이면 유사 회문
            if check_left or check_right:
                return 1
            else:
                return 2


T = int(read())

for _ in range(T):
    string = read().rstrip()
    print(palindrome(string, 0, len(string) - 1, False))
