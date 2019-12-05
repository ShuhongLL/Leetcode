class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.result = 0
        self.dfs(root, 0)
        return self.result

    def dfs(self, node: TreeNode, depth: int):
        if node:
            self.dfs(node.left, depth+1)
            self.dfs(node.right, depth+1)
        else:
            self.result = max(self.result, depth)
