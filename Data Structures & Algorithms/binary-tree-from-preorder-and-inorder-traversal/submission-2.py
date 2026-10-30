# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: i for i, val in enumerate(inorder)}
        pre = iter(preorder)

        def build(low, high):
            if low > high:
                return None
            
            val = next(pre)
            index = inorder_index[val]

            root = TreeNode(val)
            root.left = build(low, index - 1)
            root.right = build(index + 1, high)
            return root

        return build(0, len(preorder) - 1)