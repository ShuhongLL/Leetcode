# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针: fast = 2*slow
        # 2*(x+y) = x + y + n(y+z)
        # 化简：x = n(y+z) - y = (n-1)(y+z) + z
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 找出相遇点
            if slow == fast:
                slow = head
                # 从相遇点和head重新计算cycle起始点
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
