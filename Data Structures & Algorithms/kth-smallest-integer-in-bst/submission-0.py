# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []

        def dfs(node):
            if not node:
                return None

            dfs(node.left)
            in_order.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return in_order[k - 1]