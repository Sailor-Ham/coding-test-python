# 프로그래머스 12909 - 올바른 괄호

def solution(s):
    stack = []

    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False

            stack.pop()

    if stack:
        return False

    return True


s1 = "()()"
s2 = "(())()"
s3 = ")()("
s4 = "(()("

print("정답: True, 답변:", solution(s1))
print("정답: True, 답변:", solution(s2))
print("정답: False, 답변:", solution(s3))
print("정답: False, 답변:", solution(s4))
