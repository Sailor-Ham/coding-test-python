# 백준 1158 - 요세푸스 문제

import sys

input = sys.stdin.readline


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self, val):
        new_node = Node(val)

        self.head = new_node
        self.tail = new_node

    def append(self, val):
        new_node = Node(val)

        self.tail.next = new_node
        self.tail = new_node

    def close_circle(self):
        self.tail.next = self.head

    def pop(self, k):
        start = self.head

        if k == 1:
            self.head = start.next
            return start.data

        for _ in range(k - 2):
            start = start.next

        target = start.next

        start.next = target.next
        self.head = target.next

        return target.data


N, K = map(int, input().split())

circle = LinkedList(1)

for i in range(2, N + 1):
    circle.append(i)

circle.close_circle()

josephus_array = []

for _ in range(N):
    josephus_array.append(circle.pop(K))

print(f"<{', '.join(map(str, josephus_array))}>")
