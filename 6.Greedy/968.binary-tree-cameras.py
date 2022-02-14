# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # intuition:
    #   if a node has its children covered and has a parent
    #   then it is strictly better to place the camera at this node's parent

    #   if a node has children that are not covered by a camera
    #   then we must place a camera here
    def minCameraCover(self, root: TreeNode) -> int:
        self.result = 0
        self.covered = {None}
        self.dfs(root)
        return self.result

    def dfs(self, node: TreeNode, parent: TreeNode = None):
        if not node:
            return
        self.dfs(node.left, node)
        self.dfs(node.right, node)
        if (parent is None and node not in self.covered) or\
           (node.left not in self.covered or node.right not in self.covered):
            self.result += 1
            self.covered.update({node.left, node.right, node, parent})
