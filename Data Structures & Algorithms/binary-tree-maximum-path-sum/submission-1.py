# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = root.val

        def dfs(node):
            nonlocal best
            if not node:
                return 0
            left_best = max(0, dfs(node.left))
            right_best = max(0, dfs(node.right))
            best = max(best, node.val + left_best + right_best)
            return node.val + max(left_best, right_best)

        dfs(root)
        return best