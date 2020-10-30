# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def has_cycle(head: ListNode) -> bool:
        limit = 10000
        pos_count = {}
        current = head
        for i in range(0, limit):
            if current.next is None:
                return False
            if current not in pos_count:
                pos_count[current] = 0
                current = current.next
            else:
                return True
        return False
