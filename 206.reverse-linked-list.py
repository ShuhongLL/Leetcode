#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if not head:
        #     return
        # stack = []
        # cur = head
        # prev = ListNode(-1)
        # prev.next = head
        # while cur:
        #     prev.next = None
        #     prev = cur
        #     stack.append(cur)
        #     cur = cur.next
        # for i in range(len(stack)-1, 0, -1):
        #     stack[i].next = stack[i-1]
        # stack[0].next = None
        # return stack[-1]
 
        cur = head
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

# @lc code=end

