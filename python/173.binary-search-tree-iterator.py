#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class BSTIterator:

    def __init__(self, root: TreeNode):
        self._root = root
        self._queue = collections.deque([])
        self._insert_node(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self._queue.popleft().val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self._queue) != 0
    
    def _insert_node(self, root: TreeNode):
        if not root:
            return
        if root.left:
            self._insert_node(root.left)
        self._queue.append(root)
        if root.right:
            self._insert_node(root.right)
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

