# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pivot = ListNode(-1)
        pivot.next = head
        cur = pivot
        
        while cur.next and cur.next.next:
            fst = cur.next
            sec = cur.next.next
            
            cur.next = sec
            fst.next = sec.next
            sec.next = fst
            cur = fst
        return pivot.next
