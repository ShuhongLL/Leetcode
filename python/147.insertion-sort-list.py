#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        queue = []
        cur = head
        while cur:
            queue.append(cur)
            cur = cur.next
        for i in range(1, len(queue)):
            pivot = queue[i]
            j = i - 1
            while j >= 0 and pivot.val < queue[j].val:
                queue[j + 1] = queue[j]
                j -= 1
            queue[j + 1] = pivot
        for i in range(len(queue) - 1):
            queue[i].next = queue[i + 1]
        queue[-1].next = None
        return queue[0]
    
# @lc code=end

