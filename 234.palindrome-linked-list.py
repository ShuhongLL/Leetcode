# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # method 1: O(n) space
        if not head:
            return True
        # cur = head
        # s = []
        # while cur:
        #     s.append(cur.val)
        #     cur = cur.next
        # return s == s[::-1]
        
        # method 2: O(1) space
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        cur = head
        s = ''
        r = False
        while cur:
            if r:
                s += str(cur.val)[::-1]
            else:
                s += str(cur.val)
            if cur == slow:
                r = True
            cur = cur.next
        return s == s[::-1]
