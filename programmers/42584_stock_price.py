# 프로그래머스 42584 - 주식가격

from collections import deque


def solution(prices):
    answer = []
    prices_queue = deque(prices)

    while prices_queue:
        cur_price = prices_queue.popleft()
        period = 0

        for next_price in prices_queue:
            if cur_price > next_price:
                break

            period += 1

        answer.append(period)

    return answer


prices = [1, 2, 3, 2, 3]

print(solution(prices))
