# 백준 1158 - 요세푸스 문제

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def solve_josephus(self, K):
        result = []
        cur = self.head
        prev = self.tail

        while cur.next != cur:
            for _ in range(K - 1):
                prev = cur
                cur = cur.next

            result.append(cur.data)
            prev.next = cur.next
            cur = prev.next

        # 마지막 남은 하나의 cur도 순열에 넣어줘야 함
        result.append(cur.data)
        return result


read = sys.stdin.readline

N, K = map(int, read().split())
circular_linked_list = CircularLinkedList()

for i in range(1, N + 1):
    circular_linked_list.append(i)

josephus_list = circular_linked_list.solve_josephus(K)

print(f"<{', '.join(map(str, josephus_list))}>")
