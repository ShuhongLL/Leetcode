# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.result = []
        if not root:
            return
        self.dfs(root, [])
        return self.result

    def dfs(self, node: TreeNode, path: List[int]):
        if not node.left and not node.right:
            self.result.append('->'.join(path + [str(node.val)]))
        else:
            if node.left:
                self.dfs(node.left, path + [str(node.val)])
            if node.right:
                self.dfs(node.right, path + [str(node.val)])
