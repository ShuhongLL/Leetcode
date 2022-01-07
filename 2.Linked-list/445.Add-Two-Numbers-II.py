class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def reverse_list(node): 
            """Reverse a linked list."""
            prev = None
            while node:
                prev, node.next, node = node, prev, node.next
            return prev 
        
        def add_node(l1, l2, carry):
            val = l1.val + l2.val + carry
            carry = val // 10
            cur = ListNode(val % 10)
            
            if carry != 0 or l1.next or l2.next:
                if not l1.next:
                    l1.next = ListNode(0)
                if not l2.next:
                    l2.next = ListNode(0)
                cur.next = add_node(l1.next, l2.next, carry)
            return cur
                    
        
        l1, l2 = reverse_list(l1), reverse_list(l2) # reverse l1 & l2
        re_result = add_node(l1, l2, 0)
        return reverse_list(re_result)
