# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

#     method 1: recursion
#     def flipEquiv(self, root1, root2):
#         if root1 is root2:
#             return True
#         if not root1 or not root2 or root1.val != root2.val:
#             return False

#         return (self.flipEquiv(root1.left, root2.left) and
#                 self.flipEquiv(root1.right, root2.right) or
#                 self.flipEquiv(root1.left, root2.right) and
#                 self.flipEquiv(root1.right, root2.left))
    
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        node1, node2 = [], []
        self.flatten(root1, node1)
        self.flatten(root2, node2)
        return sorted(node1) == sorted(node2)
        
    def flatten(self, root: TreeNode, result: List[TreeNode]):
        children = []
        if root.left:
            children.append(root.left.val)
            self.flatten(root.left, result)
        if root.right:
            children.append(root.right.val)
            self.flatten(root.right, result)
        result.append(sorted([root.val] + children))
