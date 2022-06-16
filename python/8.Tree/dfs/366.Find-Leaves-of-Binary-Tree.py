# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def dfs(node):
            depth_l, depth_r = 0, 0
            if node.left:
                depth_l = dfs(node.left)
            if node.right:
                depth_r = dfs(node.right)
            depth = max(depth_l, depth_r)
            if len(result) <= depth:
                result.append([])
            result[depth].append(node.val)
            return depth+1
        
        dfs(root)
        return result
