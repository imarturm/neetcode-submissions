# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            if left_depth is False or right_depth is False or abs(left_depth - right_depth) > 1:
                return False
            return max(left_depth, right_depth) + 1
        return True if not root or dfs(root) else False