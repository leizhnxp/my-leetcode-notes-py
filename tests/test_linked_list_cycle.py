from solutions.linked_list_cycle import Solution, ListNode


class TestLinkedListNode:

    # 输入：head = [3,2,0,-4], pos = 1
    # 输出：true
    # 解释：链表中有一个环，其尾部连接到第二个节点。
    def test_linked_list_cycle(self):
        head = ListNode(3)
        current = head
        current.next = ListNode(2)
        current = end = current.next
        current.next = ListNode(0)
        current = current.next
        current.next = ListNode(-4)
        current = current.next
        current.next = end

        expect = Solution.has_cycle(head)
        assert expect

    # 输入：head = [1], pos = -1
    # 输出：false
    # 解释：链表中没有环。
    def test_linked_list_cycle_false(self):
        head = ListNode(1)

        expect = Solution.has_cycle(head)
        assert expect is False

    def test_linked_list_cycle_true_1_2_n1(self):
        head = ListNode(1)
        current = head
        current.next = ListNode(2)

        expect = Solution.has_cycle(head)
        assert expect is False
