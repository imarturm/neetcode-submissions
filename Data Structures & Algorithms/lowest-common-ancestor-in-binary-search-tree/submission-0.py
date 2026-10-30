# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def binary_search(p: TreeNode) -> List[TreeNode]:
            res = []
            cur = root
            while True:
                res.append(cur)
                if cur is p:
                    return res
                if cur.val > p.val:
                    cur = cur.left
                else:
                    cur = cur.right
        
        p_path = set(binary_search(p))
        for node in reversed(binary_search(q)):
            if node in p_path:
                return node